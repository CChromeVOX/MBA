# Generated by Django 3.2.16 on 2022-12-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_student_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='login',
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
