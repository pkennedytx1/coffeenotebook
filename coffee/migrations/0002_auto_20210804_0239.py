# Generated by Django 2.1.4 on 2021-08-04 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
