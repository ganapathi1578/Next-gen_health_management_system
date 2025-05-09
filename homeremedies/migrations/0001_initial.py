# Generated by Django 3.0 on 2025-03-23 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diseases', to='homeremedies.BodyPart')),
            ],
        ),
        migrations.CreateModel(
            name='Remedy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remedies', to='homeremedies.Disease')),
            ],
        ),
    ]
