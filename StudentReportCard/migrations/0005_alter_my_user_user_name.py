# Generated by Django 4.2 on 2023-08-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentReportCard', '0004_student_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
