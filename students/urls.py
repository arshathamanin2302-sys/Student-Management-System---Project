from django.urls import path
from .import views

app_name='students'

urlpatterns=[
    path('',views.list_Students, name='list'),
    path('add/',views.add_Student, name='add'),
    path('edit/<int:pk>/',views.edit_Student, name='edit'),
    path('delete/<int:pk>/',views.delete_Student, name='delete'),
]