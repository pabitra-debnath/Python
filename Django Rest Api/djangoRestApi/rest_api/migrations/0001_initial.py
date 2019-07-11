# Generated by Django 2.2.3 on 2019-07-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=10)),
                ('lastName', models.CharField(max_length=10)),
                ('emp_id', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
