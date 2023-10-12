from django.contrib import admin
from django.urls import path, re_path
from app_becas.views.signup import Signup
from app_becas.views.signin import Signin
from app_becas.views.home import Home
import app_becas.views.reports as hr
from app_becas.views.calendar import Calendar
from app_becas.views.calendar_add import Calendar_add
from app_becas.views.calendar_show_info import Calendar_show_info
from app_becas.views.manage_user import Manage_user
from app_becas.views.manage_user_2 import Manage_user_2
from app_becas.views.scholarship import Scholarship
from app_becas.views.add_scholarship import Add_scholarship
from app_becas.views.all_scholarships import All_scholarships
from app_becas.views.add_type_scholarship import AddTypeScholarship
from django.conf import settings
from django.views.static import serve
from app_becas.views.delete_type_scholarship import DeleteTypeScholarship
from app_becas.views.show_scholarship_info import Show_scholarship_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signin.as_view(), name=''),
    path('home/', Home.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signout/', Home.signout, name='signout'),

    path('calendar/', Calendar.as_view(), name='calendar'),
    path('calendar_add/', Calendar_add.as_view(), name='calendar_add'),
    path('calendar_show_info/', Calendar_show_info.as_view(), name='calendar_show_info'),
    path('delete_calendar/', Calendar_show_info.delete_calendar, name='delete_calendar'),
    path('calendar_update/', Calendar_show_info.update_calendar, name='calendar_update'),

    path('scholarship/', Scholarship.as_view(), name='scholarship'),
    path('add_scholarship/', Add_scholarship.as_view(), name='add_scholarship'),
    path('all_scholarships/', All_scholarships.as_view(), name ='all_scholarships'),
    path('add_scholarship/add_type_scholarship/', AddTypeScholarship.as_view(), name ='add_type_scholarship'),
    path('add_scholarship/delete_type_scholarship/', DeleteTypeScholarship.as_view(), name ='delete_type_scholarship'),
    path('show_scholarship_info/', Show_scholarship_info.as_view(), name='show_scholarship_info'),

    path('manage_user/', Manage_user.as_view(), name='manage_user'),
    path('manage_user_2/', Manage_user_2.as_view(), name='manage_user_2'),

    path('reports/', hr.home, name='reports'),
    path('reports_upload/', hr.upload_report, name='upload_report'),
    path('reports_external/', hr.external_reports, name='external_reports'),
    path('reports_generate/', hr.generate_report, name='generate_report'),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]
