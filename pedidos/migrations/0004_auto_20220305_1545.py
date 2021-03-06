# Generated by Django 3.2.10 on 2022-03-05 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_clientemodel_slug'),
        ('pedidos', '0003_auto_20220305_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidomodel',
            name='status',
            field=models.CharField(blank=True, choices=[('Pendente', 'Pendente'), ('Saiu para entrega', 'Saiu para entrega'), ('Entregue', 'Entregue')], max_length=17),
        ),
        migrations.AlterField(
            model_name='pedidomodel',
            name='var_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.clientemodel', verbose_name='Cliente'),
        ),
    ]
