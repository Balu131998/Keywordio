from django.urls import path
from . import views
urlpatterns=[
    path("", views.home, name='home'),
    path("Register", views.Register, name='Register'),
    path("login", views.login, name='login'),
    path("ViewBook", views.ViewBook, name='ViewBook'),
    path("AddBook", views.AddBook, name='AddBook'),
    path("UpdateBook<int:id>", views.UpdateBook, name='UpdateBook'),
    path("Delete<int:id>", views.Delete, name='Delete'),
    path("StudentProfile", views.StudentProfile, name='StudentProfile'),
    path("AdminProfile", views.AdminProfile, name='AdminProfile'),
    path("Logout", views.Logout, name='Logout'),

]