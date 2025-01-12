"""easy_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import easy_study.views as es_v
import easy_study.admin as es_a
import users.views as users_views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jatmanis1', es_v.jatmanis1, name= 'jatmanis1'),
    path('', es_v.index, name= '/'),
    path('signup', users_views.register ),
    path('login', users_views.login1 ),
    path('logout', LogoutView.as_view(), name='logout'),
    path('verify', es_v.verify, name='verify'),

    path('admin_1', es_a.admin ),
    path('notes', es_v.notes ),
    path('reader/<u_id>', es_v.reader ),
    path('test2', es_v.test2 ),
    path('test3', es_v.test3 ),
    # path('pdf', es_v.proxy_pdf),
    
    path('admin_course', es_a.admin_course),
    path('admin_course_edit', es_a.admin_course_edit, name='admin_course_edit'),
    path('admin_course_add', es_a.admin_course_add, name='admin_course_add'),
    # part 
    path('admin_part', es_a.admin_part),
    path('admin_part_edit/<int:p_id>/', es_a.admin_part_edit, name='admin_part_edit'),
    path('admin_part_add', es_a.admin_part_add, name='admin_part_add'),
    
    # subject 
    path('admin_subject', es_a.admin_subject),
    path('admin_subject_edit/<int:s_id>/', es_a.admin_subject_edit, name='admin_subject_edit'),
    path('admin_subject_add', es_a.admin_subject_add, name='admin_subject_add'),
    
    # unit
    path('admin_unit', es_a.admin_unit),
    path('admin_unit_edit/<int:u_id>/', es_a.admin_unit_edit, name='admin_unit_edit'),
    path('admin_unit_add', es_a.admin_unit_add, name='admin_unit_add'),
    # path('documents/<str:file_id>/', es_v.stream_gdrive_document, name='stream_gdrive_document'),
]