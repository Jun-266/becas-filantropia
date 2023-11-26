from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from app_becas.views.signup import Signup
from app_becas.views.signin import Signin
from app_becas.views.home import Home
import app_becas.views.reports as rp
from app_becas.views.calendar import Calendar
from app_becas.views.calendar_add import Calendar_add
from app_becas.views.calendar_show_info import Calendar_show_info
from app_becas.views.manage_student import Manage_student
from app_becas.views.manageuser import ManageUser
from app_becas.views.manage_donor import Manage_donor
from app_becas.views.manage_contact import Manage_contact
from app_becas.views.scholarship import Scholarship
from app_becas.views.add_scholarship import Add_scholarship
from app_becas.views.add_type_to_scholarship import AddTypeToScholarship
from app_becas.views.delete_user import Delete_user
from app_becas.views.modify_user import Modify_user
from app_becas.views.add_type_scholarship import AddTypeScholarship
from django.views.static import serve
from app_becas.views.delete_type_scholarship import DeleteTypeScholarship
from app_becas.views.show_scholarship_info import Show_scholarship_info
from app_becas.views.delete_donor import Delete_donor
from app_becas.views.modify_donor import Modify_donor
from app_becas.views.delete_contact import Delete_contact
from app_becas.views.modify_contact import Modify_contact
from app_becas.views.delete_student import Delete_student
from app_becas.views.modify_student import Modify_student
from app_becas.views.add_major import Add_major
from app_becas.views.delete_donor_contact import Delete_donor_contact
from app_becas.views.delete_donor_scholarship import Delete_donor_scholarship


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signin.as_view(), name=''),
    path('home/', Home.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signout/', Home.signout, name='signout'),

    # Calendar
    path('calendar/', Calendar.as_view(), name='calendar'),
    path('calendar_add/', Calendar_add.as_view(), name='calendar_add'),
    path('calendar_show_info/', Calendar_show_info.as_view(), name='calendar_show_info'),
    path('delete_calendar/', Calendar_show_info.delete_calendar, name='delete_calendar'),
    path('calendar_update/', Calendar_show_info.update_calendar, name='calendar_update'),
    
    # Scholarship
    path('scholarship/', Scholarship.as_view(), name='scholarship'),
    path('show_scholarship_info/', Show_scholarship_info.as_view(), name='show_scholarship_info'),
    path('add_scholarship/', Add_scholarship.as_view(), name='add_scholarship'),
    path('add_scholarship/add_type_scholarship/', AddTypeScholarship.as_view(),
         name='add_type_scholarship'),
    path('add_scholarship/delete_type_scholarship/', DeleteTypeScholarship.as_view(),
         name='delete_type_scholarship'),
    path('add_type_to_scholarship/', AddTypeToScholarship.as_view(), name='add_type_to_scholarship'),
    path('delete_scholarship/', Show_scholarship_info.delete_scholarship, name='delete_scholarship'),
    path('update_scholarship/', Show_scholarship_info.update_scholarship, name='update_scholarship'),

    # Reports.
    path('reports/', rp.home, name='reports'),
    path('reports/<int:file_id>', rp.delete_report, name='delete_report'),
    path('reports_upload/', rp.upload_report, name='upload_report'),
    path('list_of_candidates/', rp.render_list_of_candidates, name='loc'),
    path('list_of_candidates/generate/', rp.generate_list_of_candidates, name='g_loc'),
    path('report_scholarship_students/', rp.scholarship_students_report, name='rv_scholarship_students'),
    path('report_scholarship_students/generate/', rp.generate_report_scholarship_students,
         name='generate_scholarship_students'),

    # User
    path('manage_user/', ManageUser.as_view(), name='manage_user'),
    path('manage_student/', Manage_student.as_view(), name='manage_student'),
    path('manage_user/delete_user/<str:auto_id>/', Delete_user.as_view(), name='delete_user'),
    path('manage_contact/', Manage_contact.as_view(), name='manage_contact'),
    path('manage_user/modify_user/<str:auto_id>/', Modify_user.as_view(), name='modify_user'),
    path('manage_donor/', Manage_donor.as_view(), name='manage_donor'),
    path('manage_donor/delete_donor/<str:auto_id>/', Delete_donor.as_view(), name='delete_donor'),
    path('manage_donor/modify_donor/<str:auto_id>/', Modify_donor.as_view(), name='modify_donor'),
    path('manage_contact/delete_contact/<str:auto_id>/', Delete_contact.as_view(), name='delete_contact'),
    path('manage_contact/modify_contact/<str:auto_id>/', Modify_contact.as_view(), name='modify_contact'),
    path('manage_student/delete_student/<str:auto_id>/', Delete_student.as_view(), name='delete_student'),
    path('manage_student/modify_student/<str:auto_id>/', Modify_student.as_view(), name='modify_student'),
    path('manage_student/add_major/', Add_major.as_view(), name='add_major'),
    path('manage_donor/modify_donor/<str:auto_id>/donor_contact/<str:contact_auto_id>/',
         Delete_donor_contact.as_view(), name='delete_donor_contact'),
    path('manage_donor/modify_donor/<str:auto_id>/donor_scholarship/<str:scholarship_auto_id>/',
         Delete_donor_scholarship.as_view(), name='delete_donor_scholarship'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
