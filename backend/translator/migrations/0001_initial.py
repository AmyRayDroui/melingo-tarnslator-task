# Generated by Django 4.2.7 on 2023-11-22 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('MelingoId', models.IntegerField(primary_key=True, serialize=False)),
                ('Entry', models.CharField(max_length=255)),
                ('TranslationFull', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Text', models.CharField(max_length=500)),
                ('MelingoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='translator.entry')),
            ],
        ),
    ]