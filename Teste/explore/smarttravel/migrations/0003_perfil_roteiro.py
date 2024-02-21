# Generated by Django 5.0.1 on 2024-02-20 23:51

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarttravel', '0002_cidade_imagem_local_imagem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_modificacao', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('telefone', models.CharField(blank=True, max_length=14)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Roteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_viagem', models.DateField()),
                ('quantidade_pessoas', models.PositiveIntegerField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smarttravel.local')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
