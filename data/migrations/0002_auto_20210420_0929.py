# Generated by Django 3.1.5 on 2021-04-20 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Course', 'Course'), ('Rental', 'Rental'), ('Service', 'Service')], default='Course', max_length=7)),
                ('name', models.TextField(help_text='Course Name', max_length=100)),
                ('description', models.TextField(help_text='Course Description', max_length=400)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('current_occupancy', models.IntegerField(default=0)),
                ('maximum_occupancy', models.IntegerField(default=10)),
                ('location', models.TextField(default='Main Building', max_length=100)),
            ],
            options={
                'ordering': ['start_time', 'name'],
            },
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='booking',
            name='for_offering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.offering'),
        ),
    ]
