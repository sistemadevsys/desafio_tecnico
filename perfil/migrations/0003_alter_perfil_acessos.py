# Generated by Django 3.2.4 on 2021-06-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_perfil_acessos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='acessos',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
