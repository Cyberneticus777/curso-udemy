# Generated by Django 2.2.3 on 2019-07-14 03:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190710_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-criado'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor.fields.RichTextField(verbose_name='Conteúdo'),
        ),
    ]