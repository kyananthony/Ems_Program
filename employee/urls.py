from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('', views.view_employees, name='view_employees'),
    path('update/<int:emp_id>/', views.update_employee, name='update_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
]
