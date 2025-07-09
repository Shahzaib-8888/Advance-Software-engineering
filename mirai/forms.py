"""Defines Django ModelForm classes for Company and Employee models."""

from django import forms
from mirai.models import Employee, Company

class EmployeeForm(forms.ModelForm):
    """
    Form for creating and updating Employee instances.

    Uses all fields from the Employee model.
    """
    class Meta:
        model = Employee
        fields = "__all__"

class CompanyForm(forms.ModelForm):
    """
    Form for creating and updating Company instances.

    Uses all fields from the Company model.
    """
    class Meta:
        model = Company
        fields = "__all__"
