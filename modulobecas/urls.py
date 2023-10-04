from django.contrib import admin
from django.urls import path
from app_becas.views.signup import Signup
from app_becas.views.signin import Signin
from app_becas.views.home import Home
import app_becas.views.reports as hr
import app_becas.views.scholarship_type as sct
from app_becas.views.calendar import Calendar
from app_becas.views.calendar_add import Calendar_add
from app_becas.views.calendar_show_info import Calendar_show_info
from app_becas.views.manage_user import Manage_user
from app_becas.views.scholarship import Scholarship

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signin.as_view(), name=''),
    path('home/', Home.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signout/', Home.signout, name='signout'),
    path('calendar/', Calendar.as_view(), name='calendar'),
    path('calendar_add/', Calendar_add.as_view(), name='calendar_add'),
    path('calendar_show_info/', Calendar_show_info.as_view(), name='calendar_show_info'),
    path('manage_user/', Manage_user.as_view(), name='manage_user'),
    path('scholarship/', Scholarship.as_view(), name='scholarship'),
    path('reports/', hr.home, name='reports'),
    path('reports_upload/', hr.upload_report, name='upload_report'),
    path('reports_external/', hr.external_reports, name='external_reports'),
    path('reports_generate/', hr.generate_report, name='generate_report'),
    path('scholarship_type/', sct.home_scholarship, name='scholarship_type_home'),
]
