# Generated by Django 4.2.7 on 2023-12-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amz', '0004_remove_produto_id_pro_remove_produto_idade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.TextField(max_length=12),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.IntegerField(default=None),
        ),
    ]