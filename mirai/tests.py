"""Automated tests for the Company and Employee models."""

from django.test import TestCase
from .models import Company, Employee
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

class CompanyModelTest(TestCase):
    """
    Test cases for the Company model, covering creation, uniqueness,
    string representation, blank field allowance, and email validation.
    """

    def test_create_company(self):
        """Test creating a company with all required fields."""
        company = Company.objects.create(
            cName="Test Co", cEmail="test@example.com", cLogo="", cUrl="http://test.com"
        )
        self.assertEqual(company.cName, "Test Co")
        self.assertEqual(company.cEmail, "test@example.com")

    def test_company_str(self):
        """Test the string representation (__str__) of a company."""
        company = Company.objects.create(
            cName="ACME", cEmail="acme@corp.com", cLogo="", cUrl="http://acme.com"
        )
        self.assertEqual(str(company), "ACME" if hasattr(company, "__str__") else company.cName)

    def test_unique_company_name(self):
        """Test that company names must be unique."""
        Company.objects.create(cName="Unique", cEmail="a@a.com", cLogo="", cUrl="a.com")
        with self.assertRaises(IntegrityError):
            Company.objects.create(cName="Unique", cEmail="b@b.com", cLogo="", cUrl="b.com")

    def test_blank_logo_allowed(self):
        """Test that the logo field can be left blank."""
        company = Company.objects.create(
            cName="LogoLess", cEmail="logo@less.com", cLogo="", cUrl="logo.com"
        )
        self.assertEqual(company.cLogo, "")

    def test_invalid_email(self):
        """Test that an invalid email raises a ValidationError."""
        company = Company(
            cName="BadEmail", cEmail="not-an-email", cLogo="", cUrl="bad.com"
        )
        with self.assertRaises(ValidationError):
            company.full_clean()

class EmployeeModelTest(TestCase):
    """
    Test cases for the Employee model, covering creation, required fields,
    relationship behavior, blank fields, and uniqueness.
    """

    def setUp(self):
        """Set up a sample company for use in employee tests."""
        self.company = Company.objects.create(
            cName="Test Co", cEmail="test@example.com", cLogo="", cUrl="http://test.com"
        )

    def test_create_employee(self):
        """Test creating an employee and linking to a company."""
        emp = Employee.objects.create(
            eFname="Ali", eLname="Khan", eCompany=self.company, eEmail="ali@test.com", ePhone="123456"
        )
        self.assertEqual(emp.eFname, "Ali")
        self.assertEqual(emp.eCompany, self.company)

    def test_employee_email_required(self):
        """Test that employee email is required."""
        emp = Employee(
            eFname="NoMail", eLname="Khan", eCompany=self.company, eEmail="", ePhone="123456"
        )
        with self.assertRaises(ValidationError):
            emp.full_clean()

    def test_delete_company_cascades_to_employee(self):
        """Test that deleting a company also deletes its employees."""
        emp = Employee.objects.create(
            eFname="DelTest", eLname="Bye", eCompany=self.company, eEmail="del@test.com", ePhone="98765"
        )
        self.company.delete()
        self.assertEqual(Employee.objects.filter(eFname="DelTest").count(), 0)

    def test_employee_phone_can_be_blank(self):
        """Test that employee phone field can be left blank."""
        emp = Employee.objects.create(
            eFname="PhoneBlank", eLname="Smith", eCompany=self.company, eEmail="phone@blank.com", ePhone=""
        )
        self.assertEqual(emp.ePhone, "")

    def test_employee_unique_firstname(self):
        """
        Test that employee first names are unique.
        This will only pass if eFname is set to unique=True in the model,
        which may not be realistic in production
        """
        Employee.objects.create(
            eFname="UniqueF", eLname="Smith", eCompany=self.company, eEmail="a@a.com", ePhone="111"
        )
        with self.assertRaises(IntegrityError):
            Employee.objects.create(
                eFname="UniqueF", eLname="Different", eCompany=self.company, eEmail="b@b.com", ePhone="222"
            )
