# Generated by Django 4.1.5 on 2023-01-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_customeruser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='password2',
            field=models.CharField(default='default password2', max_length=255),
            preserve_default=False,
        ),
    ]