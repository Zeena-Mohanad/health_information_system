from django.contrib import admin
from health.models import Patients, Symptoms, Illness, Treatment, MedicalReport, IllnessTreatment, TreatmentTypes, Pills

@admin.register(Patients)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'gender']
    search_fields = ['first_name', 'last_name']

@admin.register(Symptoms)
class SymptomsAdmin(admin.ModelAdmin):
    list_display = ['symptoms', 'description']
    search_fields = ['symptoms']

@admin.register(Illness)
class IllnessAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(MedicalReport)
class MedicineReportAdmin(admin.ModelAdmin):
    list_display = ['patient', 'report_file', 'date']
    search_fields = ['patient__first_name', 'patient__last_name', 'report_file']

@admin.register(IllnessTreatment)
class IllnessTreatmentAdmin(admin.ModelAdmin):
    list_display = ['illness', 'treatment', 'duration', 'details']
    search_fields = ['illness__name', 'treatment__name']

@admin.register(TreatmentTypes)
class TreatmentTypesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Pills)
class PillsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
