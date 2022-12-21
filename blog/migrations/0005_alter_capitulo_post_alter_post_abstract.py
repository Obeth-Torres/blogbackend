# Generated by Django 4.1.3 on 2022-11-24 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_capitulo_options_capitulo_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(default=''),
        ),
    ]
