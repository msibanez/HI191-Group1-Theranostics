# Generated by Django 4.0.4 on 2023-01-18 19:24

from django.db import migrations, models
import django.db.models.deletion
import part_1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoneScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metastasis_status', models.CharField(choices=[('Metastasis', 'Metastasis'), ('No Metastasis', 'No Metastasis')], max_length=120)),
                ('sg_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Fdgpetct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fdgpetct_img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gapsma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(choices=[('GA-68', 'GA-68'), ('F-18 PSMA', 'F-18 PSMA')], max_length=120)),
                ('gapsma_img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesion_status', models.CharField(choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('size', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecog_score', models.IntegerField(blank=True)),
                ('height', models.IntegerField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('bmi', models.IntegerField(blank=True)),
                ('bp', models.IntegerField(blank=True)),
                ('hr', models.IntegerField(blank=True)),
                ('pain_score', models.IntegerField(blank=True)),
                ('local_symptoms', models.CharField(blank=True, max_length=300)),
                ('systemic_symptoms', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SalivaryGland',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Normal', 'Normal'), ('Left Obstruction', 'Left Obstruction'), ('Right Obstruction', 'Right Obstruction')], max_length=120)),
                ('sg_image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rs', models.ImageField(blank=True, upload_to='')),
                ('psa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('creatinine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('wbc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rbc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hemoglobin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hematocrit', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('platelet', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lactate_hydrogenase', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('alkaline_phosphatase', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sgpt', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sgot', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bilirubins', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bonescan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.bonescan')),
                ('fdgpetct', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.fdgpetct')),
                ('gapsma', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.gapsma')),
                ('salivarygland', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.salivarygland')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('patient_code', part_1.models.AutoIncrementField(blank=True, editable=False, null=True)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('diagnosis_date', models.DateField()),
                ('surgery_date', models.DateField()),
                ('histopath_result', models.ImageField(upload_to='')),
                ('date_of_treatment', models.DateField()),
                ('type_of_treatment', models.CharField(choices=[('Hormonal Treatment', 'Hormonal Treatment'), ('Radiation Therapy', 'Radiation Therapy'), ('Chemotherapy', 'Chemotherapy'), ('Others', 'Others')], max_length=120)),
                ('physical_exam', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.physicalexam')),
            ],
        ),
        migrations.AddField(
            model_name='gapsma',
            name='lesion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.lesion'),
        ),
        migrations.AddField(
            model_name='fdgpetct',
            name='lesion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='part_1.lesion'),
        ),
    ]
