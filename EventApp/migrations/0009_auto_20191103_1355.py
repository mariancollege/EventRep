# Generated by Django 2.2.5 on 2019-11-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0008_auto_20191102_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('eventid', models.TextField(primary_key=True, serialize=False)),
                ('eventname', models.CharField(max_length=25)),
                ('venue', models.TextField()),
                ('date', models.DateField()),
                ('regfee', models.IntegerField()),
                ('tpm', models.IntegerField()),
                ('department', models.TextField()),
                ('descreption', models.TextField()),
                ('brochure', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='addmin',
        ),
        migrations.DeleteModel(
            name='user',
        ),

    ]
