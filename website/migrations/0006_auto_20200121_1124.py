# Generated by Django 3.0.1 on 2020-01-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200121_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default='posts/dj_default.jpg', upload_to='posts'),
        ),
    ]