import requests

from django.shortcuts import render, redirect

from .models import Transacao
from .forms import TransacaoForm


def calcular_posicao(ticker, quantidade):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    response = requests.get(url, headers=headers)
    data = response.json()

    try:
        preco_atual = data['chart']['result'][0]['indicators']['quote'][0]['open'][-1]
    except (KeyError, IndexError):
        preco_atual = None

    if preco_atual:
        return preco_atual * quantidade
    else:
        return None


def carteira(request):
    transacoes = Transacao.objects.all()
    total_investido = 0

    for transacao in transacoes:
        transacao.posicao_atual = calcular_posicao(
            transacao.ticker, transacao.quantidade)
        total_investido += transacao.preco_compra * transacao.quantidade

    posicao_carteira = sum(
        [transacao.posicao_atual for transacao in transacoes])
    lucro = posicao_carteira - total_investido

    return render(request, 'carteira/carteira.html', {
        'transacoes': transacoes,
        'total_investido': total_investido,
        'posicao_carteira': posicao_carteira,
        'lucro': lucro,
        'range': range(len(transacoes)),
        'form': TransacaoForm(),
    })


def adicionar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            preco_compra = float(form.cleaned_data['preco_compra'])
            quantidade = int(form.cleaned_data['quantidade'])
            form.instance.total = preco_compra * quantidade
            form.save()
    return redirect('carteira')
