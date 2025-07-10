# Employee & Company Management System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.1-blueviolet?logo=bootstrap)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern, secure, and scalable Employee & Company Management System built with Django and Bootstrap. This project provides a professional solution for managing company and employee records, with full CRUD functionality, user authentication, and robust data integrity.

---

## 📸 Screenshots

![111](https://github.com/user-attachments/assets/1946e1d2-16fd-4e26-9766-4d3c09f9642b)

![222](https://github.com/user-attachments/assets/d053de21-a985-4b2b-9043-79916d547f18)

![333](https://github.com/user-attachments/assets/9e04a666-f99d-4d76-b290-6154f777ff14)

![444](https://github.com/user-attachments/assets/75641c9c-505c-4710-aae0-7a5188b0ee5b)

![555](https://github.com/user-attachments/assets/32db9404-8ac0-4dca-8200-0125e9cb611c)

![666](https://github.com/user-attachments/assets/84815ec2-bec8-4c73-843a-1e5d28146799)

![777](https://github.com/user-attachments/assets/35a61a21-1c2a-4b54-8041-0b1065e32b0c)

---

## 🚀 Features

- **Secure Authentication:** Only registered users can manage records.
- **Company Management:** Create, view, edit, and delete company records.
- **Employee Management:** Manage employee details, assign to companies.
- **Cascading Deletes:** Deleting a company removes its employees (no orphaned records).
- **Bootstrap UI:** Fully responsive and mobile-friendly.
- **Comprehensive Testing:** Automated tests for all critical functions.
- **Cloud Deployable:** Ready for deployment on Render, Heroku, etc.

---

## ⚙️ Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Shahzaib-8888/Advance-Software-engineering.git
   cd Advance-Software-engineering
   ```

2. **Clone the Repository:**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```
   
3. **Install Dependencies::**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (for Admin Login):**
   ```bash
   python manage.py createsuperuser
   ```
   
6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   
7. **Access the App**
   ```bash
   Open http://127.0.0.1:8000/ in your browser.
   ```

---

## 🔑 Usage

- **Login** using your admin credentials.
- **Add Companies and Employees** via the menu.
- **Edit and Delete** records with confirmation prompts.
- All management actions are protected — only authenticated users can access them.

---

## 🧪 Testing

To run all test cases and verify functionality, use the following command:

```bash
python manage.py test
```

---

## ☁️ Deployment

Easily deploy on Render by following these steps:

1. **Add `requirements.txt` and `Procfile` to your repository.**
2. **Set up `DATABASE_URL` and `SECRET_KEY` as environment variables** on your deployment platform.
3. **Configure static files in `settings.py`.**
   - Make sure `STATIC_ROOT` and `MEDIA_ROOT` are set appropriately.
   - Run `python manage.py collectstatic` before deploying.
4. **For Render:**  
   See the [official Django deployment guide](https://render.com/docs/deploy-django) for detailed steps.

---

## 🗄️ Database Schema

| **Company Table**    | **Employee Table**           |
|----------------------|-----------------------------|
| id (PK)              | id (PK)                     |
| cName (unique)       | eFname                      |
| cEmail               | eLname                      |
| cLogo (optional)     | eCompany (FK → Company)     |
| cUrl                 | eEmail                      |
|                      | ePhone                      |

---

## 👨‍💻 Authors

- Shahzaib Tahir
- [Shahzaib-8888](https://github.com/Shahzaib-8888)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📚 References

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Bootstrap Documentation](https://getbootstrap.com/)



