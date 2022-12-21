# Generated by Django 4.1.3 on 2022-12-15 14:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='cap_body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='sub_body1',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='sub_body2',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='sub_body3',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
    ]
