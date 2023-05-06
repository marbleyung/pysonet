# Generated by Django 4.2 on 2023-05-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_usernet_bio_usernet_date_of_birth_usernet_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usernet',
            name='technology',
            field=models.ManyToManyField(related_name='users', to='profiles.technology'),
        ),
    ]