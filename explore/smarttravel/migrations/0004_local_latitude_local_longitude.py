# Generated by Django 5.0.1 on 2024-02-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarttravel', '0003_alter_local_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
