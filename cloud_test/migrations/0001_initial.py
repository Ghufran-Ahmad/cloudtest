# Generated by Django 2.0.4 on 2018-04-22 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=60)),
                ('lName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=60)),
                ('Password', models.CharField(max_length=60)),
                ('dp', models.ImageField(upload_to='')),
            ],
        ),

        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.PositiveIntegerField()),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('bedSize', models.CharField(max_length=60)),
                ('wifi', models.BooleanField()),
                ('roomService', models.BooleanField()),
                ('breakfast', models.BooleanField()),
                ('pool', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='typeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud_test.Types'),
        ),
    ]
