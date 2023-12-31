from django.conf import settings
from django.conf.urls.static import static
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
from app_becas.views.manage_donor import Manage_donor
from app_becas.views.manage_contact import Manage_contact
from app_becas.views.scholarship import Scholarship
from app_becas.views.add_scholarship import Add_scholarship
from app_becas.views.delete_user import Delete_user
from app_becas.views.modify_user import Modify_user
from app_becas.views.add_type_scholarship import AddTypeScholarship
from django.views.static import serve
from app_becas.views.delete_type_scholarship import DeleteTypeScholarship
from app_becas.views.show_scholarship_info import Show_scholarship_info
from app_becas.views.search_scholarship import SearchScholarship
from app_becas.views.delete_donor import Delete_donor
from app_becas.views.modify_donor import Modify_donor
from app_becas.views.delete_contact import Delete_contact
from app_becas.views.modify_contact import Modify_contact


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
    path('show_scholarship_info/', Show_scholarship_info.as_view(), name='show_scholarship_info'),
    path('add_scholarship/', Add_scholarship.as_view(), name='add_scholarship'),
    path('add_scholarship/add_type_scholarship/', AddTypeScholarship.as_view(), name='add_type_scholarship'),
    path('add_scholarship/delete_type_scholarship/', DeleteTypeScholarship.as_view(), name='delete_type_scholarship'),
    path('search_scholarship/', SearchScholarship.as_view(), name='search_scholarship'),

    path('reports/', hr.home, name='reports'),
    path('reports/<int:file_id>', hr.delete_report, name='delete_report'),
    path('reports_upload/', hr.upload_report, name='upload_report'),
    path('reports_external/', hr.external_reports, name='external_reports'),
    path('reports_generate/', hr.generate_report, name='generate_report'),
    
    path('manage_user/', Manage_user.as_view(), name='manage_user'),
    path('manage_user/delete_user/<str:auto_id>/', Delete_user.as_view(), name='delete_user'),
    path('manage_contact/', Manage_contact.as_view(), name='manage_contact'),
    path('manage_user/modify_user/<str:auto_id>/', Modify_user.as_view(), name='modify_user'),
    path('manage_donor/', Manage_donor.as_view(), name='manage_donor'),
    path('manage_donor/delete_donor/<str:auto_id>/', Delete_donor.as_view(), name='delete_donor'),
    path('manage_donor/modify_donor/<str:auto_id>/', Modify_donor.as_view(), name='modify_donor'),
    path('manage_contact/delete_contact/<str:auto_id>/', Delete_contact.as_view(), name='delete_contact'),
    path('manage_contact/modify_contact/<str:auto_id>/', Modify_contact.as_view(), name='modify_contact'),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

