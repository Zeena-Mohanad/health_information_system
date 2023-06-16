# Generated by Django 4.1.6 on 2023-06-16 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_illnesstreatment_medicalreport_patients_pills_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatment',
            old_name='patient',
            new_name='ilness_patient_id',
        ),
        migrations.RemoveField(
            model_name='illness',
            name='patient',
        ),
        migrations.CreateModel(
            name='IllnessPatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('illness_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.illness')),
                ('patients_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.patients')),
            ],
        ),
        migrations.AddField(
            model_name='illness',
            name='patient',
            field=models.ManyToManyField(through='health.IllnessPatients', to='health.patients'),
        ),
    ]