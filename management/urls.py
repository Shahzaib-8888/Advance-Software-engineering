"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""URL configuration for the Employee Management System.

Maps URLs to corresponding view functions for company and employee management,
authentication, and static/media file handling.
"""

from django.contrib import admin
from django.urls import path, include
from mirai import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),

    # --- Company URLs ---
    path('comp', views.comp, name='comp'),                         # Add company
    path('show', views.show, name='show'),                         # List companies
    path('edit/<int:pk>', views.edit, name='edit'),                # Edit company
    path('update/<int:pk>', views.update, name='update'),           # Update company
    path('delete/<int:pk>', views.delete, name='delete'),           # Delete company

    # --- Employee URLs ---
    path('emp', views.emp, name='emp'),                            # Add employee
    path('showemp', views.showemp, name='showemp'),                # List employees
    path('editemp/<int:pk>', views.editemp, name='editemp'),       # Edit employee
    path('updateEmp/<int:pk>', views.updateEmp, name='updateEmp'), # Update employee
    path('deleteEmp/<int:pk>', views.deleteEmp, name='deleteEmp'), # Delete employee

    # --- Home page ---
    path('', views.home, name='home'),

    # --- Authentication URLs ---
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
