# Generated by Django 3.0.4 on 2020-03-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmae', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
