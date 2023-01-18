# Generated by Django 4.0.4 on 2023-01-18 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='physical_exam',
        ),
        migrations.AddField(
            model_name='physicalexam',
            name='patient_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part_1.patient'),
        ),
        migrations.AddField(
            model_name='screening',
            name='patient_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part_1.patient'),
        ),
    ]
