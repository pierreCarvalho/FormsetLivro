# Generated by Django 2.1.5 on 2019-05-29 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_autor', models.CharField(max_length=40, verbose_name='Nome do autor')),
                ('tel_fixo', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefone Fixo')),
                ('tel_celular', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefone Celular')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livro.Livro')),
            ],
        ),
    ]