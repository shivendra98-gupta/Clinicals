from django import forms 
from .models import Patient,ClinicalData


# FORMS.PY ISLIYE BANAYA JISSSE DATA UPDATE KAR SAKEH
class PatientForm(forms.Form):
    class Meta:
        model=Patient
        fields="__all__"

class ClinicalDataForm(forms.Form):
    class Meta:
        model=ClinicalData
        fields="__all__"