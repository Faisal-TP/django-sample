# Generated by Django 3.0.4 on 2021-02-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajax_crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjaxFileUpd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('file', models.CharField(max_length=100)),
            ],
        ),
    ]
