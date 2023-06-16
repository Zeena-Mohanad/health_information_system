from ninja import Router
from health.models import IllnessTreatment, Patients, Symptoms, Illness, Treatment, MedicalReport, TreatmentTypes
from health.schemas import IllnessTreatmentSchema, PatientSchema, SymptomsSchema, IllnessSchema, TreatmentSchema, MedicineReportSchema, TreatmentTypesSchema

router = Router()

# Patient CRUD endpoints
@router.post("/patients")
def create_patient(request, payload: PatientSchema):
    patient_data = payload.dict()
    try:
        patient = Patients.objects.create(**patient_data)
    except Exception as e:
        return {"error": str(e)}
    patient_schema = PatientSchema.from_orm(patient)
    return patient_schema.dict()

@router.get("/patients/{patient_id}")
def get_patient(request, patient_id: int):
    try:
        patient = Patients.objects.get(id=patient_id)
    except Patients.DoesNotExist:
        return {"error": "Patient not found"}
    patient_schema = PatientSchema.from_orm(patient)
    return patient_schema.dict()

@router.put("/patients/{patient_id}")
def update_patient(request, patient_id: int, payload: PatientSchema):
    try:
        patient = Patients.objects.get(id=patient_id)
    except Patients.DoesNotExist:
        return {"error": "Patient not found"}
    patient_data = payload.dict()
    try:
        for key, value in patient_data.items():
            setattr(patient, key, value)
        patient.save()
    except Exception as e:
        return {"error": str(e)}
    patient_schema = PatientSchema.from_orm(patient)
    return patient_schema.dict()

@router.delete("/patients/{patient_id}")
def delete_patient(request, patient_id: int):
    try:
        patient = Patients.objects.get(id=patient_id)
    except Patients.DoesNotExist:
        return {"error": "Patient not found"}
    patient.delete()
    return {"message": "Patient deleted successfully"}

# Symptoms CRUD endpoints
@router.post("/symptoms")
def create_symptoms(request, payload: SymptomsSchema):
    symptoms_data = payload.dict()
    try:
        symptoms = Symptoms.objects.create(**symptoms_data)
    except Exception as e:
        return {"error": str(e)}
    symptoms_schema = SymptomsSchema.from_orm(symptoms)
    return symptoms_schema.dict()

@router.get("/symptoms/{symptoms_id}")
def get_symptoms(request, symptoms_id: int):
    try:
        symptoms = Symptoms.objects.get(id=symptoms_id)
    except Symptoms.DoesNotExist:
        return {"error": "Symptoms not found"}
    symptoms_schema = SymptomsSchema.from_orm(symptoms)
    return symptoms_schema.dict()

@router.put("/symptoms/{symptoms_id}")
def update_symptoms(request, symptoms_id: int, payload: SymptomsSchema):
    try:
        symptoms = Symptoms.objects.get(id=symptoms_id)
    except Symptoms.DoesNotExist:
        return {"error": "Symptoms not found"}
    symptoms_data = payload.dict()
    try:
        for key, value in symptoms_data.items():
            setattr(symptoms, key, value)
        symptoms.save()
    except Exception as e:
        return {"error": str(e)}
    symptoms_schema = SymptomsSchema.from_orm(symptoms)
    return symptoms_schema.dict()

@router.delete("/symptoms/{symptoms_id}")
def delete_symptoms(request, symptoms_id: int):
    try:
        symptoms = Symptoms.objects.get(id=symptoms_id)
    except Symptoms.DoesNotExist:
        return {"error": "Symptoms not found"}
    symptoms.delete()
    return {"message": "Symptoms deleted successfully"}

# Illness CRUD endpoints
@router.post("/illnesses")
def create_illness(request, payload: IllnessSchema):
    illness_data = payload.dict()
    try:
        illness = Illness.objects.create(**illness_data)
    except Exception as e:
        return {"error": str(e)}
    illness_schema = IllnessSchema.from_orm(illness)
    return illness_schema.dict()

@router.get("/illnesses/{illness_id}")
def get_illness(request, illness_id: int):
    try:
        illness = Illness.objects.get(id=illness_id)
    except Illness.DoesNotExist:
        return {"error": "Illness not found"}
    illness_schema = IllnessSchema.from_orm(illness)
    return illness_schema.dict()

@router.put("/illnesses/{illness_id}")
def update_illness(request, illness_id: int, payload: IllnessSchema):
    try:
        illness = Illness.objects.get(id=illness_id)
    except Illness.DoesNotExist:
        return {"error": "Illness not found"}
    illness_data = payload.dict()
    try:
        for key, value in illness_data.items():
            setattr(illness, key, value)
        illness.save()
    except Exception as e:
        return {"error": str(e)}
    illness_schema = IllnessSchema.from_orm(illness)
    return illness_schema.dict()

@router.delete("/illnesses/{illness_id}")
def delete_illness(request, illness_id: int):
    try:
        illness = Illness.objects.get(id=illness_id)
    except Illness.DoesNotExist:
        return {"error": "Illness not found"}
    illness.delete()
    return {"message": "Illness deleted successfully"}

# Treatment CRUD endpoints
@router.post("/treatments")
def create_treatment(request, payload: TreatmentSchema):
    treatment_data = payload.dict()
    try:
        drugs_ids = treatment_data.pop('drugs', [])
        treatment = Treatment.objects.create(**treatment_data)
        treatment.drugs.set(drugs_ids)
    except Exception as e:
        return {"error": str(e)}
    treatment_schema = TreatmentSchema.from_orm(treatment)
    return treatment_schema.dict()

@router.get("/treatments/{treatment_id}")
def get_treatment(request, treatment_id: int):
    try:
        treatment = Treatment.objects.get(id=treatment_id)
    except Treatment.DoesNotExist:
        return {"error": "Treatment not found"}
    treatment_schema = TreatmentSchema.from_orm(treatment)
    return treatment_schema.dict()

@router.put("/treatments/{treatment_id}")
def update_treatment(request, treatment_id: int, payload: TreatmentSchema):
    try:
        treatment = Treatment.objects.get(id=treatment_id)
    except Treatment.DoesNotExist:
        return {"error": "Treatment not found"}
    treatment_data = payload.dict()
    try:
        drugs_ids = treatment_data.pop('drugs', [])
        for key, value in treatment_data.items():
            setattr(treatment, key, value)
        treatment.save()
        treatment.drugs.set(drugs_ids)
    except Exception as e:
        return {"error": str(e)}
    treatment_schema = TreatmentSchema.from_orm(treatment)
    return treatment_schema.dict()

@router.delete("/treatments/{treatment_id}")
def delete_treatment(request, treatment_id: int):
    try:
        treatment = Treatment.objects.get(id=treatment_id)
    except Treatment.DoesNotExist:
        return {"error": "Treatment not found"}
    treatment.delete()
    return {"message": "Treatment deleted successfully"}

# MedicalReport CRUD endpoints
@router.post("/MedicalReports")
def create_medical_report(request, payload: MedicineReportSchema):
    report_data = payload.dict()
    try:
        report = MedicalReport.objects.create(**report_data)
    except Exception as e:
        return {"error": str(e)}
    report_schema = MedicineReportSchema.from_orm(report)
    return report_schema.dict()

@router.get("/MedicalReports/{medicine_report_id}")
def get_medical_report(request, medicine_report_id: int):
    try:
        report = MedicalReport.objects.get(id=medicine_report_id)
    except MedicalReport.DoesNotExist:
        return {"error": "Medical Report not found"}
    report_schema = MedicineReportSchema.from_orm(report)
    return report_schema.dict()

@router.put("/MedicalReports/{medicine_report_id}")
def update_medical_report(request, medicine_report_id: int, payload: MedicineReportSchema):
    try:
        report = MedicalReport.objects.get(id=medicine_report_id)
    except MedicalReport.DoesNotExist:
        return {"error": "Medical Report not found"}
    report_data = payload.dict()
    try:
        for key, value in report_data.items():
            setattr(report, key, value)
        report.save()
    except Exception as e:
        return {"error": str(e)}
    report_schema = MedicineReportSchema.from_orm(report)
    return report_schema.dict()

@router.delete("/MedicalReports/{medicine_report_id}")
def delete_medical_report(request, medicine_report_id: int):
    try:
        report = MedicalReport.objects.get(id=medicine_report_id)
    except MedicalReport.DoesNotExist:
        return {"error": "Medical Report not found"}
    report.delete()
    return {"message": "Medical Report deleted successfully"}

# IllnessTreatment CRUD endpoints
@router.post("/illness-treatments")
def create_illness_treatment(request, payload: IllnessTreatmentSchema):
    illness_treatment_data = payload.dict()
    try:
        illness_treatment = IllnessTreatment.objects.create(**illness_treatment_data)
    except Exception as e:
        return {"error": str(e)}
    illness_treatment_schema = IllnessTreatmentSchema.from_orm(illness_treatment)
    return illness_treatment_schema.dict()

@router.get("/illness-treatments/{illness_treatment_id}")
def get_illness_treatment(request, illness_treatment_id: int):
    try:
        illness_treatment = IllnessTreatment.objects.get(id=illness_treatment_id)
    except IllnessTreatment.DoesNotExist:
        return {"error": "Illness Treatment not found"}
    illness_treatment_schema = IllnessTreatmentSchema.from_orm(illness_treatment)
    return illness_treatment_schema.dict()

@router.put("/illness-treatments/{illness_treatment_id}")
def update_illness_treatment(request, illness_treatment_id: int, payload: IllnessTreatmentSchema):
    try:
        illness_treatment = IllnessTreatment.objects.get(id=illness_treatment_id)
    except IllnessTreatment.DoesNotExist:
        return {"error": "Illness Treatment not found"}
    illness_treatment_data = payload.dict()
    try:
        for key, value in illness_treatment_data.items():
            setattr(illness_treatment, key, value)
        illness_treatment.save()
    except Exception as e:
        return {"error": str(e)}
    illness_treatment_schema = IllnessTreatmentSchema.from_orm(illness_treatment)
    return illness_treatment_schema.dict()

@router.delete("/illness-treatments/{illness_treatment_id}")
def delete_illness_treatment(request, illness_treatment_id: int):
    try:
        illness_treatment = IllnessTreatment.objects.get(id=illness_treatment_id)
    except IllnessTreatment.DoesNotExist:
        return {"error": "Illness Treatment not found"}
    illness_treatment.delete()
    return {"message": "Illness Treatment deleted successfully"}

# TreatmentTypes CRUD endpoints
@router.post("/treatment-types")
def create_treatment_type(request, payload: TreatmentTypesSchema):
    treatment_type_data = payload.dict()
    try:
        treatment_type = TreatmentTypes.objects.create(**treatment_type_data)
    except Exception as e:
        return {"error": str(e)}
    treatment_type_schema = TreatmentTypesSchema.from_orm(treatment_type)
    return treatment_type_schema.dict()

@router.get("/treatment-types/{treatment_type_id}")
def get_treatment_type(request, treatment_type_id: int):
    try:
        treatment_type = TreatmentTypes.objects.get(id=treatment_type_id)
    except TreatmentTypes.DoesNotExist:
        return {"error": "Treatment Type not found"}
    treatment_type_schema = TreatmentTypesSchema.from_orm(treatment_type)
    return treatment_type_schema.dict()

@router.put("/treatment-types/{treatment_type_id}")
def update_treatment_type(request, treatment_type_id: int, payload: TreatmentTypesSchema):
    try:
        treatment_type = TreatmentTypes.objects.get(id=treatment_type_id)
    except TreatmentTypes.DoesNotExist:
        return {"error": "Treatment Type not found"}
    treatment_type_data = payload.dict()
    try:
        for key, value in treatment_type_data.items():
            setattr(treatment_type, key, value)
        treatment_type.save()
    except Exception as e:
        return {"error": str(e)}
    treatment_type_schema = TreatmentTypesSchema.from_orm(treatment_type)
    return treatment_type_schema.dict()

@router.delete("/treatment-types/{treatment_type_id}")
def delete_treatment_type(request, treatment_type_id: int):
    try:
        treatment_type = TreatmentTypes.objects.get(id=treatment_type_id)
    except TreatmentTypes.DoesNotExist:
        return {"error": "Treatment Type not found"}
    treatment_type.delete()
    return {"message": "Treatment Type deleted successfully"}


