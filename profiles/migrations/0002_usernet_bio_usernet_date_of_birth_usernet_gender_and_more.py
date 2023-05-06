# Generated by Django 4.2 on 2023-05-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernet',
            name='bio',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-binary', 'Non-binary')], null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
