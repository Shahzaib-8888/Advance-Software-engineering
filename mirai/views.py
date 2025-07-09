"""Defines all view functions for company and employee management.

Includes CRUD operations, authentication checks, and user feedback messages.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mirai.models import Company, Employee
from mirai.forms import CompanyForm, EmployeeForm

def home(request):
    """
    Render the home page for the application.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse with rendered home page.
    """
    return render(request, "home.html")

# ----- Company Views -----

@login_required
def comp(request):
    """
    Handle the creation of a new company.

    Renders the company creation form and processes submitted data.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse with form or redirect to the company list.
    """
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Company created successfully.")
            return redirect('show')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form': form})

@login_required
def show(request):
    """
    Display all companies.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse with company list.
    """
    companies = Company.objects.all()
    return render(request, "show.html", {'companies': companies})

@login_required
def edit(request, pk):
    """
    Render the edit form for a company.

    Args:
        request: HttpRequest object.
        pk: Primary key of the company.

    Returns:
        HttpResponse with edit form.
    """
    company = get_object_or_404(Company, pk=pk)
    form = CompanyForm(instance=company)
    return render(request, "edit.html", {'form': form, 'company': company})

@login_required
def update(request, pk):
    """
    Handle company updates.

    Args:
        request: HttpRequest object.
        pk: Primary key of the company.

    Returns:
        HttpResponse with updated form or redirect.
    """
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, "Company updated successfully.")
            return redirect('show')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CompanyForm(instance=company)
    return render(request, "edit.html", {'form': form, 'company': company})

@login_required
def delete(request, pk):
    """
    Delete a company by primary key and redirect to the company list.

    Args:
        request: HttpRequest object.
        pk: Primary key of the company.

    Returns:
        HttpResponse redirect.
    """
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    messages.success(request, "Company deleted successfully.")
    return redirect('show')

# ----- Employee Views -----

@login_required
def emp(request):
    """
    Handle the creation of a new employee.

    Renders the employee creation form and processes submitted data.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse with form or redirect to the employee list.
    """
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect('showemp')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form': form})

@login_required
def showemp(request):
    """
    Display all employees.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse with employee list.
    """
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees': employees})

@login_required
def editemp(request, pk):
    """
    Render the edit form for an employee.

    Args:
        request: HttpRequest object.
        pk: Primary key of the employee.

    Returns:
        HttpResponse with edit form.
    """
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(instance=employee)
    return render(request, "editemployee.html", {'form': form, 'employee': employee})

@login_required
def updateEmp(request, pk):
    """
    Handle employee updates.

    Args:
        request: HttpRequest object.
        pk: Primary key of the employee.

    Returns:
        HttpResponse with updated form or redirect.
    """
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect('showemp')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "editemployee.html", {'form': form, 'employee': employee})

@login_required
def deleteEmp(request, pk):
    """
    Delete an employee by primary key and redirect to the employee list.

    Args:
        request: HttpRequest object.
        pk: Primary key of the employee.

    Returns:
        HttpResponse redirect.
    """
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('showemp')
