# Generated by Django 4.2.7 on 2023-12-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amz', '0007_alter_produto_categoria_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo_pro',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
