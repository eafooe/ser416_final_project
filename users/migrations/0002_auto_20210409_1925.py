# Generated by Django 3.1.5 on 2021-04-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Member', 'Member'), ('Volunteer', 'Volunteer'), ('Employee', 'Employee')], default='member', max_length=9),
        ),
    ]
