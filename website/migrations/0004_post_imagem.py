# Generated by Django 3.0.1 on 2020-01-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default='dj_default.jpeg', upload_to='posts'),
        ),
    ]
