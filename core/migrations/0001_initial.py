# Generated by Django 3.1.3 on 2020-11-22 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Markets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Selections',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('odds', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField()),
                ('markets', models.ManyToManyField(to='core.Markets')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sport')),
            ],
        ),
        migrations.AddField(
            model_name='markets',
            name='selections',
            field=models.ManyToManyField(to='core.Selections'),
        ),
    ]
