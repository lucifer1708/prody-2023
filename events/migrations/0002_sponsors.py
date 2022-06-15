# Generated by Django 4.0.4 on 2022-06-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sponsors/')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=30)),
            ],
        ),
    ]