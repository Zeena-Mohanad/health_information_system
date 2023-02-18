from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

class Symptoms(models.Model):
    symptoms = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symptoms

class Illness(models.Model):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    symptoms = models.ManyToManyField(Symptoms)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
        
class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name 
    
class MedicineReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)
    report_file = models.FileField(upload_to='medicine_reports/')
    report_name = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.patient) + " - " + self.report_name   