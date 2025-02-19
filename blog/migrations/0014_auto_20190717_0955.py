# Generated by Django 2.1 on 2019-07-17 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post1_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='content',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post1',
            name='title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
