# Generated by Django 3.2.4 on 2022-05-06 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('date_creation', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=200, null=True)),
                ('Prénoms_client', models.CharField(max_length=200, null=True)),
                ('zone', models.CharField(max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200)),
                ('latitude', models.CharField(blank=True, max_length=200)),
                ('date_creation', models.DateField(auto_now=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fs.agent')),
            ],
        ),
    ]
