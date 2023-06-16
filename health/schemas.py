from datetime import date
import datetime
from ninja import Schema
from marshmallow import fields
from json import JSONEncoder
from typing import Optional

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)

class PatientSchema(Schema):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    phone_no: Optional[int]
    id: Optional[int]

class SymptomsSchema(Schema):
    symptoms: str
    description: Optional[str]
    degree: Optional[str]

class IllnessSchema(Schema):
    name: str
    description: str
    symptoms: list[SymptomsSchema]
    patient_id: int
    id: Optional[int]

class PillsSchema(Schema):
    name: str   
    
class TreatmentSchema(Schema):
    patient_id: int
    name: str
    description: str
    pills: list[PillsSchema]
    illness_id: list[IllnessSchema]
    treatment_types_id: int
    id: Optional[int]

class MedicineReportSchema(Schema):
    patient_id: int
    illness_id: int
    report_file: str
    date: date

class IllnessTreatmentSchema(Schema):
    illness_id: int
    treatment_id: int
    duration: Optional[str]
    deatils: Optional[str]
    
class TreatmentTypesSchema(Schema):
    name: str    

class IllnessPatientSchema(Schema):
    patient_id :int
    illness_id :int
    date: date
    
class IllnessSymptomsSchema(Schema):
    illness_id :int 
    symptoms_id :int
    
class PatientTreatmentSchema(Schema):
    treatment_id: int
    illness_patient_id: int             
# Set the custom encoder as the default JSON encoder
Schema.json_encoder = CustomJSONEncoder
