# Generated by Django 2.0 on 2017-12-27 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platformes', '0005_auto_20171226_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='favorited',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='feedback',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_ago',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_now',
            field=models.FloatField(null=True),
        ),
    ]
