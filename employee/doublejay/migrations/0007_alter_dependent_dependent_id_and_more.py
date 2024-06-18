# Generated by Django 4.2.6 on 2024-01-31 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doublejay', '0006_alter_dependent_dependent_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependent',
            name='Dependent_id',
            field=models.CharField(default='DE536', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_id',
            field=models.CharField(default='E827', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(default='P944', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='works_on',
            name='work_id',
            field=models.CharField(default='W842', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]