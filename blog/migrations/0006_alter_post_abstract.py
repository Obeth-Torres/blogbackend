# Generated by Django 4.1.3 on 2022-11-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_capitulo_post_alter_post_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(),
        ),
    ]
