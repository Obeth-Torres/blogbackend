# Generated by Django 4.1.3 on 2022-12-08 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_capitulo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='cita1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita4',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita5',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita6',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita7',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cita8',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='referencias1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='referencias2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='referencias3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='referencias4',
            field=models.TextField(blank=True, default=''),
        ),
    ]
