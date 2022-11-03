from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='faculties'),
    path('upload_faculties', views.upload_file, name='upload_faculties')
]
