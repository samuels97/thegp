# Generated by Django 3.2.3 on 2022-01-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0008_alter_post_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='viewers',
            field=models.IntegerField(default=1, null=True),
        ),
    ]