# Generated by Django 2.1.3 on 2018-11-10 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='amount',
        ),
        migrations.AddField(
            model_name='recipes',
            name='description',
            field=models.TextField(default=datetime.datetime(2018, 11, 10, 17, 43, 2, 194825, tzinfo=utc)),
            preserve_default=False,
        ),
    ]