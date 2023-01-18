# Generated by Django 4.0.4 on 2023-01-18 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0004_alter_patient_patient_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screening',
            name='bonescan',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='fdgpetct',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='gapsma',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='salivarygland',
        ),
        migrations.AddField(
            model_name='patient',
            name='alkaline_phosphatase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='bilirubins',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='bmi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='bp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='ecog_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gleason_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='hematocrit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='hemoglobin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='hr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='lactate_hydrogenase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='local_symptoms',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='patient',
            name='metastasis_status',
            field=models.CharField(blank=True, choices=[('Metastasis', 'Metastasis'), ('No Metastasis', 'No Metastasis')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='pain_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='platelet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='psa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='rbc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='rs',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='salivarygland',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part_1.salivarygland'),
        ),
        migrations.AddField(
            model_name='patient',
            name='sg_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='sgot',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='sgpt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='systemic_symptoms',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='patient',
            name='wbc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='type_of_treatment',
            field=models.CharField(choices=[('Low Risk', 'Low Risk'), ('Intermediate Risk', 'Intermediate Risk'), ('High Risk', 'High Risk')], max_length=120),
        ),
        migrations.DeleteModel(
            name='PhysicalExam',
        ),
        migrations.DeleteModel(
            name='Screening',
        ),
    ]
