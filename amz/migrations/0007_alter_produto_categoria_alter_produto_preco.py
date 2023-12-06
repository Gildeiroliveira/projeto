# Generated by Django 4.2.7 on 2023-12-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amz', '0006_alter_produto_codigo_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.TextField(default='Sem mais detalhes', max_length=12),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
