from django.contrib import admin

from health.models import Patient, Symptoms, Illness, Treatment, MedicineReport

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    
    

admin.site.register(Patient, PatientAdmin)
admin.site.register(Symptoms)
admin.site.register(Illness)
admin.site.register(Treatment)
admin.site.register(MedicineReport)