from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
def ViewBook(request):
    book = Book.objects.all()
    context={'book':book}
    return render(request, "ViewBook.html",context)
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user_obj = UserProfile.objects.filter(email=email).first()
        if user_obj is None:
            messages.success(request, ("User is not registered"))
            print("no user")
            return redirect('Register')

        user = authenticate(email=email, password=password)
        if user is None:
            messages.success(request, ("Login failed"))
            print("no")
            return redirect('login')

        login(request, user)
        if user.is_staff:
            return redirect('Admin')
        else:
            return redirect('student')

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect("home")


def Register(request):
    if request.method == "POST":
        fname = request.POST["first"]
        last = request.POST["last"]

        pwd = request.POST["password"]
        em = request.POST["email"]
        con = request.POST["phone"]
        tp = request.POST["utype"]
        try:
            UserProfile.objects.get(email=em)
            messages.success(request, ("Email already registered"))
            print("Email already registered")
        except UserProfile.DoesNotExist:
            usr = UserProfile.objects.create_user(em, pwd)
            usr.first_name = fname
            usr.last_name = last
            if tp == "admin":
                usr.is_staff = True
                usr.save()

            reg = register(user=usr, phone=con, user_type=tp)
            reg.save()
            messages.success(request, ("User Registered Successfully"))
    return render(request, 'Registration.html')

def StudentProfile(request):
    book = Book.objects.all()
    context={'book':book}
    return render(request, "student.html", context)


def AdminProfile(request):
    return render(request, 'Admin.html')

#
def AddBook(request):
    if request.method == "POST":
        id = request.POST.get('id')
        Title = request.POST.get('Title')
        Author = request.POST.get('Author')
        Department = request.POST.get('Department')
        book = Book(id=id, Title=Title, Author=Author, Department=Department)
        book.save()
        return redirect('ViewBook')
    else:
        return render(request, 'AddBook.html')


def UpdateBook(request, id):
    book = Book.objects.get(id=id)
    context= {'book': book}
    return render(request, 'UpdateBook.html')


def Delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('ViewBook')



