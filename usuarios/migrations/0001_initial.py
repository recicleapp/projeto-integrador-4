# Generated by Django 3.2.13 on 2022-06-02 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50, verbose_name='Item')),
                ('item_description', models.CharField(blank=True, max_length=50, verbose_name='Descrição do item')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='ConsumerProfileModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/', verbose_name='Foto para o perfil')),
                ('public_place', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('number', models.CharField(default='s/n', max_length=5, verbose_name='Numero')),
                ('complement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('district', models.CharField(max_length=36, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Consumidor',
                'verbose_name_plural': 'Consumidores',
            },
        ),
        migrations.CreateModel(
            name='CollectorProfileModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/', verbose_name='Foto para o perfil')),
                ('public_place', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('number', models.CharField(default='s/n', max_length=5, verbose_name='Numero')),
                ('complement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('district', models.CharField(max_length=36, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, verbose_name='CNPJ')),
                ('home_collection', models.BooleanField(default=False, verbose_name='Coleta em domicílio')),
                ('citywide_pickup', models.BooleanField(default=False, verbose_name='Coleta em toda a cidade')),
                ('works_with_disposal', models.BooleanField(default=False, verbose_name='Trabalha com descarte')),
                ('works_with_donations', models.BooleanField(default=False, verbose_name='Trabalha com doações')),
                ('collection_districts', models.ManyToManyField(to='usuarios.DistrictsModel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('worked_items', models.ManyToManyField(to='usuarios.ItemModel')),
            ],
            options={
                'verbose_name': 'Coletor',
                'verbose_name_plural': 'Coletores',
            },
        ),
        migrations.CreateModel(
            name='collaboratorProfileModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/', verbose_name='Foto para o perfil')),
                ('public_place', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('number', models.CharField(default='s/n', max_length=5, verbose_name='Numero')),
                ('complement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('district', models.CharField(max_length=36, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
    ]
