# Generated by Django 2.2 on 2020-04-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200426_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
