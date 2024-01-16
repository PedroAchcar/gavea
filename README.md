# Gávea Investimentos
Aplicação para teste de estágio da empresa Gávea Investimentos

## Autor
Nome: Pedro Francisco Ignácio Achcar

Email: pedroachcar@gmail.com / pedro.achcar@poli.ufrj.br

## Ambiente e Tecnologias
Para a linguagem foi usada a linguagem de programação Python, utilizada juntamente do framework Django para criação do backend e uso dos Django Templates para criação do frontend. Como banco de dados foi utilizado o SQLite que é criado automaticamente pelo Django ao iniciarmos a aplicação. Foi feita a integração com a API do Yahoo Finance que retorna os preços de uma ação dado o ticker dela. 

## Instalação do ambiente
Após clonar o repositório para a sua máquina e ter o Python instalado, abra o terminal do Windows (outros sistemas operacionais o comando é outro) e digite o seguinte comando para criar um ambiente virtual e o segundo para ativação do ambiente virtual:
```
python -m venv .venv
.\.venv\Scripts\activate
```
Seguinte, para instalar as bibliotecas e framework, utilizamos o comando a seguir na pasta raiz do projeto onde está o arquivo requirements.txt:
```
pip install -r requirements.txt
```
Com tudo instalado e configurado, para iniciar o servidor, utilizamos a seguinte sequência de comandos:
```
python manage.py migrate
python manage.py makemigrations carteira
python manage.p migrate
python manage.py runserver
```
Com isso, já temos nosso servidor funcionando. O Django utiliza por padrão a porta 8000 para aplicações (```http://127.0.0.1:8000/```). Aqui não precisamos de um Super User para acesso dos dados, pois não precisamos editá-los diretamente.

## Sobre o Desafio
Este projeto é uma Calculadora de Carteira desenvolvida em Django, permitindo que os usuários registrem transações de compra de ações, calculem a posição acionária, visualizem o total investido, a posição total da carteira, e verifiquem se obtiveram lucro ou prejuízo com base nos preços atuais das ações. Foi usado o módulo requests do Python para ter acesso a API do Yahoo Finance.

## Arquitetura e Design (Model, View, Template)

### Modelagem dos Dados
Utilizei somente uma entidade, que chamei de Transação. Ela contém o ticker, o preço de compra, a quantidade, o total da compra, a posição atual daquela ação e a data da transação.

### Views
Foram feitas somente duas views principais, que fazem as regras do aplicativo. A primeira é a adicionar_transacao que adiciona novas transações feitas pelo usuário no banco de dados, dados o ticker, o preço de compra e a quantidade comprada da respectiva ação, assim, ela calcula o total e salva as quatro informações no banco.
A segunda view é a carteira que, como o próprio nome sugere, dita a manipulação dos dados da carteira para envio ao frontend. Ela calcula o investimento total até o momento, a posição total da carteira e o lucro/prejuízo do usuário naquele momento.

### Template
Somente foi necessário criar um template, que é o frontend da nossa aplicação, esse template tem o nome de carteira. Ela mostra uma tabela com os cinco dados salvos em cada ação, o total investido, a posição total da carteira, o lucro ou prejuízo do usuário e tem, ao final, a parte de adicionar uma transação nova.
Nesse template, a posição de cada ação e a posição total da carteira mudam de cor de acordo com o respectivo lucro ou prejuízo, se for lucro, o valor ficará verde e, caso contrário, o valor ficará vermelho.
