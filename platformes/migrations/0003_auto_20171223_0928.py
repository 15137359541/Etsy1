# Generated by Django 2.0 on 2017-12-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platformes', '0002_goods_good_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='favorited',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='goods',
            name='feedback',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_ago',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_now',
            field=models.FloatField(),
        ),
    ]
