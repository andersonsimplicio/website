# Generated by Django 3.0.1 on 2020-01-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default='dj_default.jpg', upload_to='posts'),
        ),
    ]