"""Admin interface customizations for the Company and Employee models."""

from django.contrib import admin
from .models import Company, Employee

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Company model.

    Features:
    - Displays company name, email, logo, and URL in the admin list view.
    - Allows searching companies by name and email.
    """
    list_display = ('cName', 'cEmail', 'cLogo', 'cUrl')
    search_fields = ('cName', 'cEmail')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Employee model.

    Features:
    - Displays first name, last name, associated company, email, and phone in the admin list view.
    - Allows searching employees by first name, last name, and email.
    - Enables filtering of employees by associated company.
    """
    list_display = ('eFname', 'eLname', 'eCompany', 'eEmail', 'ePhone')
    search_fields = ('eFname', 'eLname', 'eEmail')
    list_filter = ('eCompany',)
