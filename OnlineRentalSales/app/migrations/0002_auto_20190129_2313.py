# Generated by Django 2.1.4 on 2019-01-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePlotModel',
            fields=[
                ('plotno', models.IntegerField(primary_key=True, serialize=False)),
                ('roadno', models.IntegerField(max_length=10)),
                ('surveyno', models.IntegerField(max_length=10)),
                ('costpersqyard', models.DecimalField(decimal_places=2, max_digits=10)),
                ('otherexpences', models.CharField(max_length=30)),
                ('boundaries', models.CharField(max_length=200)),
                ('facing', models.CharField(choices=[('east', 'EAST'), ('west', 'WEST')], max_length=30)),
                ('status', models.CharField(choices=[('vacant', 'VACANT'), ('reserve', 'RESERVE'), ('sold', 'SOLD')], max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='type',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('user', 'USER')], max_length=20),
        ),
    ]
