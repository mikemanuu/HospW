
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctors, name='doctors'),
    path('myservice/', views.myservice, name='myservice'),
    path('departments/', views.departments, name='departments'),
    path('show/', views.show, name='show'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('delete/<int:id>', views.delete),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('updatecontact/<int:id>', views.updatecontact, name='updatecontact'),
    path('editcontact/<int:id>', views.editcontact, name='editcontact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
