"""Defines the database models for Company and Employee in the employee management system."""

from django.db import models

class Company(models.Model):
    """
    Model representing a company.

    Fields:
        cName (str): The unique name of the company.
        cEmail (str): The company's email address.
        cLogo (Image): The company's logo image (optional).
        cUrl (str): The company's website URL.
    """
    cName = models.CharField(max_length=50, unique=True)
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="images", blank=True)
    cUrl = models.CharField(max_length=50)

    class Meta:
        db_table = "company"

    def __str__(self):
        """Returns the company name as its string representation."""
        return self.cName

class Employee(models.Model):
    """
    Model representing an employee.

    Fields:
        eFname (str): The employee's first name.
        eLname (str): The employee's last name.
        eCompany (Company): The company the employee is associated with.
        eEmail (str): The employee's email address.
        ePhone (str): The employee's phone number.
    """
    eFname = models.CharField(max_length=50)
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"

    def __str__(self):
        """Returns the employee's full name as its string representation."""
        return f"{self.eFname} {self.eLname}"
