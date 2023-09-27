"""
URL configuration for modulobecas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_becas.views.signup import Signup
from app_becas.views.signin import Signin
from app_becas.views.home import Home
import app_becas.views.reports as hr
from app_becas.views.calendar import Calendar
from app_becas.views.add_calendar import Add_calendar
from app_becas.views.manage_user import Manage_user
from app_becas.views.scholarship import Scholarship

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signin.as_view(), name=''),
    path('home/', Home.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signout/', Home.signout, name='signout'),
    path('calendar/', Calendar.as_view(), name='calendar'),
    path('add_calendar/', Add_calendar.as_view(), name='add_calendar'),
    path('manage_user/', Manage_user.as_view(), name='manage_user'),
    path('scholarship/', Scholarship.as_view(), name='scholarship'),
    path('reports/', hr.home, name='reports'),
]
