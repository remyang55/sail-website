# Generated by Django 3.0.6 on 2020-06-03 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20200603_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='room',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_time',
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Room')),
            ],
        ),
    ]
