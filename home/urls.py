from tkinter.font import names

from .import views
from django.urls import path



urlpatterns=[
    path('',views.index,name="index"),
    path('about/', views.about, name="about"),
    path('booking/', views.booking, name="booking"),
    path('doctors/', views.doctors, name="doctors"),
    path('contact/', views.contact, name="contact"),
    path('department/',views.department,name="department")

]