# Generated by Django 4.0.4 on 2022-12-05 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.studenttype'),
        ),
    ]
