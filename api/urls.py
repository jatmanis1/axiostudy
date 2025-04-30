from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='api-index'),
    path('verify/', views.verify, name='api-verify'),
    path('jatmanis1/', views.jatmanis1, name='api-jatmanis1'),
    path('notes/', views.notes, name='api-notes'),
    path('reader/<int:u_id>/', views.reader, name='api-reader'),
    path('test2/<int:u_id>/', views.test2, name='api-test2'),
    path('media/<filename>', views.serve_secure_pdf, name='api-serve_secure_pdf'),
    path('units/', views.units, name='api-units'),
    path('unit/<idx>', views.unit, name='api-unit'),
    path('unitdata/<idx>', views.unitdata, name='api-unitdata'),
]


