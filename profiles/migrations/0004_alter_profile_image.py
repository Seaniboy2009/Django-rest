# Generated by Django 3.2.18 on 2023-03-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default_profile_oq6ujj', upload_to='images/'),
        ),
    ]
