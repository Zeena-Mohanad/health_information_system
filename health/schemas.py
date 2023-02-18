from datetime import date
from ninja import Schema
from marshmallow import fields

class PatientSchema(Schema):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str

class SymptomSchema(Schema):
    name: str
    description: str

class IllnessSchema(Schema):
    name: str
    description: str
    symptoms: list[int]
    patient_id: int

class TreatmentSchema(Schema):
    patient_id: int
    drugs: list[int]
    illness_id: int

class MedicineReportSchema(Schema):
    patient_id: int
    report_file: str = fields.String()
    report_name: str
    date: date