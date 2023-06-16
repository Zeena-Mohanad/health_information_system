from django.db import models

class Patients(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    phone_no = models.IntegerField()
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

class Symptoms(models.Model):
    symptoms = models.CharField(max_length=255, default='')
    description = models.TextField(null=True)
    degree = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.symptoms

class Illness(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    symptoms = models.ManyToManyField(Symptoms)
    patient = models.ManyToManyField(Patients, through='IllnessPatients')

    def __str__(self):
        return self.name

class IllnessPatients(models.Model):
    patients_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    illness_id = models.ForeignKey(Illness, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
class Pills(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    

class TreatmentTypes(models.Model):
    name = models.CharField(max_length=255, default='')  
    
class Treatment(models.Model):
    ilness_patient_id = models.ManyToManyField(Patients)
    name = models.CharField(max_length=255)
    description = models.TextField()
    pills = models.ManyToManyField(Pills)
    illness = models.ManyToManyField(Illness, through='IllnessTreatment')
    treatment_types = models.ForeignKey(TreatmentTypes, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.name 

class IllnessTreatment(models.Model): 
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    duration = models.CharField(max_length=255)
    details = models.CharField(max_length=10000)
  
class MedicalReport(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, default=1)
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='medicine_reports/')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.patient) + " - " + self.report_name
