# Generated by Django 4.2 on 2023-07-30 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentReportCard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_marks', to='StudentReportCard.subject'),
        ),
    ]
