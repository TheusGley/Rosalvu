# Generated by Django 4.2.11 on 2025-02-28 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0005_remove_carrinho_servico_remove_carrinho_valor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto_carrinho',
            name='avaliacao',
        ),
        migrations.RemoveField(
            model_name='produto_carrinho',
            name='quantidade',
        ),
    ]
