from unittest.mock import call

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import  HttpResponse
from .forms import FromRegisterforms
from .models import Registaredfroms
from django.contrib import messages
from .models import cars
from .models import usercars
from .models import approve
from django.db import connection
from .forms import addcars
from .forms import usercars
from .forms import bookcars
from .models import bookcars
from .models import reviews
from .models import bookusercars
from .forms import bookinfouser
from .forms import usercarsinfo
from django.shortcuts import redirect
from .forms import feedback
# Create your views here.
m=0
def home(request):
    cursor = connection.cursor()
    cursor.execute("call avgreting()")
    results = cursor.fetchall()
    return render(request, 'home.html', {'reviews': results})

    #return render(request,'home.html')

def registration(request):
    if request.method=='POST':
        try:

            saverecord=Registaredfroms()
            saverecord.first_name=request.POST.get('first_name')
            saverecord.last_name=request.POST.get('last_name')
            saverecord.username=request.POST.get('username')
            saverecord.password=request.POST.get('password')
            #saverecord.confirm_password=request.POST.get('confirm_password')
            saverecord.email=request.POST.get('email')
            saverecord.gender=request.POST.get('gender')
            saverecord.phone_no=request.POST.get('phone_no')
            saverecord.save()
            messages.success(request,'Record saved successfully')
            context = {'FromRegisterforms': FromRegisterforms}
            response = HttpResponse('Registration successful')
            # set cookie to transfer user name to login success page.
            response.set_cookie('registration', 3600)

            return response
        except :
            return HttpResponse('username taken')

            #return render(request, 'registration.html')
    else:
        return render(request, 'registration.html',{})

def login(request):
    if request.method=="POST":
        try:
            userdetails=Registaredfroms.objects.get(username=request.POST['username'],password=request.POST['password'])
            print("username=",userdetails)
            return render(request, 'userfront.html')
        except Registaredfroms.DoesNotExist as e:
            return HttpResponse("username/pass invalid")
        #from django.contrib import auth
        #x=auth.authenticate(username=username1,password=password1)
        #if x is None:
         #   return redirect('login')C
        #else:
        #    return redirect('/')

    return render(request, 'login.html')

def adminlogin(request):
    if request.method=="POST":
        from django.contrib import auth
        username1=request.POST['username']
        password1=request.POST['password']
        x=auth.authenticate(username=username1,password=password1)
        if x is None:
            return HttpResponse('username/password is invalid')
        else:
            return render(request,'adminFront.html')

    return render(request, 'adminlogin.html',)

def CarAddAdmin(request):
    if request.method=='POST':
        try:

            saverecord=cars()
            saverecord.cars_name=request.POST.get('cars_name')
            saverecord.cars_model=request.POST.get('cars_model')
            saverecord.cars_number=request.POST.get('cars_number')
            saverecord.cars_colour=request.POST.get('cars_colour')
            saverecord.price=request.POST.get('price')
            saverecord.seat_number=request.POST.get('seat_number')
            saverecord.save()
            messages.success(request,'Record saved successfully')
            context = {'cars': cars}
            response = HttpResponse('Car Added successfully')
            # set cookie to transfer user name to login success page.
            response.set_cookie('cars', 3600)


        except :
            return HttpResponse('this car is already added')
    return render(request,'CarAddAdmin.html',)

def showcars(request):
    cursor=connection.cursor()
    cursor.execute("call GetCarsinfoSP()")
    results=cursor.fetchall()
    return render(request,'CarsTable.html', {'cars':results})


def editcar(request):
    cursor = connection.cursor()
    cursor.execute("call GetCarsinfoSP()")
    results = cursor.fetchall()
    return render(request, 'editcar.html', {'cars': results})


def updatecar(request,cars_number):
    displaycarsinfo=cars.objects.get(cars_number=cars_number)
    return render(request, "update.html", {"cars":displaycarsinfo})

def updatecarsinfo(request,cars_number):
    updatecarsinfo = cars.objects.filter(cars_number=cars_number)
    if request.method == "POST":
        ##try:
            form = addcars(request.POST)
            if form.is_valid():
                #form = addcars(request.POST)
                ##cars.full_clean()
                cars.objects.filter(cars_number=cars_number).delete()
                form.save()
                messages.success(request, "record updated successfully")
                #return render(request, "update.html", {"cars": updatecarsinfo})
                return HttpResponse("Information updated successfully")
        #except :
            #return HttpResponse(" except")

    return render(request, "update.html", {"cars": updatecarsinfo})



def delrec(request,cars_number):
    #updatecarsinfo = cars.objects.get(cars_number=cars_number)
    #updatecarsinfo.delete()
    cars.objects.filter(cars_number=cars_number).delete()
    cursor = connection.cursor()
    cursor.execute("call GetCarsinfoSP()")
    results = cursor.fetchall()
    return render(request, 'editcar.html', {'cars': results})

def logout(request):
    logout(request)

    return redirect('adminlogin.html')

def rent(request):
    if request.method=='POST':
        try:

            saverecord=usercars()
            saverecord.username=request.POST.get('user_name')
            saverecord.area=request.POST.get('area')
            saverecord.cars_name=request.POST.get('cars_name')
            saverecord.cars_model=request.POST.get('cars_model')
            saverecord.cars_number=request.POST.get('cars_number')
            saverecord.cars_colour=request.POST.get('cars_colour')
            saverecord.price = request.POST.get('price')
            saverecord.seat_number=request.POST.get('seat_number')
            saverecord.approval=request.POST.get('approval')
            saverecord.save()
            messages.success(request,'Record saved successfully')
            #context = {'cars': cars}
            response = HttpResponse('You have to wait for admin approval ')
            # set cookie to transfer user name to login success page.
            response.set_cookie('cars', 3600)

            return response
        except :
            return HttpResponse('this car is already added')
    return render(request, 'rent.html')


def usercarsi(request):
    cursor=connection.cursor()
    cursor.execute("call GetrentSP()")
    results=cursor.fetchall()
    return render(request,'usercarstable.html', {'usercars':results})


def notapprove(request,cars_number):
    #updatecarsinfo = usercars.objects.get(cars_number=cars_number)
    #updatecarsinfo.delete()
    usercars.objects.filter(cars_number=cars_number).delete()
    cursor = connection.cursor()
    cursor.execute("call GetrentSP()")
    results = cursor.fetchall()
    return render(request,'usercarstable.html', {'usercars':results})

def approved(request,cars_number):
    displaycarsinfo = usercars.objects.get(cars_number=cars_number)
    return render(request, "approve.html", {"usercars": displaycarsinfo})

def finalapprove(request,cars_number):
    finalapprove = usercars.objects.filter(cars_number=cars_number)
    usercars.objects.filter(cars_number=cars_number).delete()
    if request.method == "POST":

            saverecord = usercars()
            saverecord.username = request.POST.get('username')
            saverecord.area = request.POST.get('area')
            saverecord.cars_name = request.POST.get('cars_name')
            saverecord.cars_model = request.POST.get('cars_model')
            saverecord.cars_number = request.POST.get('cars_number')
            saverecord.cars_colour = request.POST.get('cars_colour')
            saverecord.price = request.POST.get('price')
            saverecord.seat_number = request.POST.get('seat_number')
            saverecord.approval = request.POST.get('approval')
            #saverecord.price=10000
            saverecord.save()
            return HttpResponse('this car is approved')


def book(request,cars_number):
    if request.method == "POST":
        try:
            userdetails = Registaredfroms.objects.get(username=request.POST['username'],
                                                      password=request.POST['password'])
            print("username=", userdetails)
        except Registaredfroms.DoesNotExist as e:
            return HttpResponse("username/pass invalid")

        saverecord = bookcars()
        saverecord.username = request.POST.get('username')
        saverecord.address = request.POST.get('address')
        saverecord.ending_date = request.POST.get('ending_date')
        saverecord.cars_number = cars_number
        saverecord.save()

        cursor = connection.cursor()
        cursor.execute("call showinfosp()")
        results = cursor.fetchall()
        return render(request, 'report.html', {'payment': results})

    return render(request, 'book.html')

def booking(request,cars_number):
    if request.method=="POST":
        try:
            userdetails=Registaredfroms.objects.get(username=request.POST['username'],password=request.POST['password'])
            print("username=",userdetails)
            return render(request, 'userfront.html' )
        except Registaredfroms.DoesNotExist as e:
            return HttpResponse("username/pass invalid")

    return HttpResponse("nothing much")

def bookusercar(request):
    cursor = connection.cursor()
    cursor.execute("call Getusercarsp()")
    results = cursor.fetchall()
    return render(request, 'bookusercar.html', {'usercars': results})

def book_userar(request,cars_number):

    if request.method == "POST":
        try:
            userdetails=Registaredfroms.objects.get(username=request.POST['username'],password=request.POST['password'])
            print("username=",userdetails)
        except Registaredfroms.DoesNotExist as e:
            return HttpResponse("username/pass invalid")

        saverecord = bookusercars()
        saverecord.username=request.POST.get('username')
        saverecord.address=request.POST.get('address')
        saverecord.ending_date=request.POST.get('ending_date')
        saverecord.cars_number=cars_number
        saverecord.save()

        cursor = connection.cursor()
        cursor.execute("call showuserbookinginfo()")
        results = cursor.fetchall()
        return render(request, 'reportuser.html', {'paymentuser': results})

    return render(request,'book.html')

def showpayment(request):
    cursor = connection.cursor()
    cursor.execute("call showinfosp()")
    results = cursor.fetchall()
    return render(request, 'report.html', {'payment': results})

def review(request):
    if request.method == "POST":
            saverecord = reviews()
            saverecord.advice = request.POST.get('advice')
            saverecord.rating = request.POST.get('rating')
            saverecord.save()
            return HttpResponse("your review received")


    return render(request, 'givereview.html')

def advices(request):
    cursor = connection.cursor()
    cursor.execute("call showadvice()")
    results = cursor.fetchall()
    return render(request, 'advices.html', {'reviews': results})