# Generated by Django 5.0.1 on 2024-01-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('preco_compra', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('posicao_atual', models.FloatField(blank=True, null=True)),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]