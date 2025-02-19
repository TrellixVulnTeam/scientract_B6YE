# Generated by Django 2.1 on 2019-07-23 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='academician',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='engineers',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='researchers',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='Category'),
        ),
    ]
