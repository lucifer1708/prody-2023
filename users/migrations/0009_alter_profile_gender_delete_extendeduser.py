# Generated by Django 4.0.4 on 2022-06-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='ExtendedUser',
        ),
    ]
