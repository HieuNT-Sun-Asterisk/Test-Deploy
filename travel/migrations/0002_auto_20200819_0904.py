# Generated by Django 3.0.8 on 2020-08-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-rating', '-create_date']},
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='images/tours'),
        ),
        migrations.AlterField(
            model_name='review',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/reviews'),
        ),
    ]
