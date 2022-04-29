# Generated by Django 3.2.10 on 2022-03-02 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='produtoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pedidoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('0', 'Pendente'), ('1', 'Saiu para entrega'), ('2', 'Entregue')], max_length=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.produtomodel')),
                ('var_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.clientemodel')),
            ],
        ),
    ]
