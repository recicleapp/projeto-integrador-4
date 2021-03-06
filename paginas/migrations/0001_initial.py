# Generated by Django 3.2.13 on 2022-06-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
