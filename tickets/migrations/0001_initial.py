# Generated by Django 5.0 on 2024-05-05 16:35

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('available_tickets', models.PositiveIntegerField(default=50)),
                ('image', models.ImageField(default='events/default.jpg', null=True, upload_to='events')),
                ('description', models.CharField(max_length=1000, null=True)),
                ('date', models.DateField(default=datetime.date(2024, 5, 5), null=True)),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True)),
                ('type', models.CharField(choices=[('CC', 'Concert'), ('CO', 'Conference'), ('AT', 'Attrations'), ('DE', 'Detente'), ('DI', 'Divertissement'), ('FO', 'Formation')], max_length=8)),
                ('public', models.CharField(choices=[('ET', 'Etudiants'), ('PR', 'Professionnel'), ('TT', 'Tout Type'), ('EF', 'Enfant'), ('AD', 'Adulte'), ('HO', 'Homme'), ('FE', 'Femme')], max_length=8)),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='TicketPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('quantity', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.event')),
            ],
        ),
    ]
