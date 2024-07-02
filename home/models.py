from datetime import datetime

from django.db import models

# Create your models here.

class Registaredfroms(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    #confirm_password=models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=11)
    class Meta:
        db_table= "registaredfroms"


class cars(models.Model):
    cars_name=models.CharField(max_length=100)
    cars_model=models.CharField(max_length=100)
    cars_number=models.CharField(max_length=100)
    cars_colour=models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    seat_number=models.CharField(max_length=3)
    class Meta:
        db_table="carsinfo"


class usercars(models.Model):
    username=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    cars_name=models.CharField(max_length=100)
    cars_model=models.CharField(max_length=100)
    cars_number=models.CharField(max_length=100)
    cars_colour=models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    seat_number=models.CharField(max_length=3)
    approval=models.CharField(max_length=100)
    class Meta:
        db_table="usercarsinfo"

class approve(models.Model):
    username = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    cars_name = models.CharField(max_length=100)
    cars_model = models.CharField(max_length=100)
    cars_number = models.CharField(max_length=100)
    cars_colour = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=3)

    class Meta:
        db_table = "approvedcars"

class bookcars(models.Model):
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    ending_date=models.DateField(max_length=100)
    cars_number=models.CharField(max_length=100)

    class Meta:
        db_table = "bookinfo"

class bookusercars(models.Model):
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    ending_date=models.DateField(max_length=100)
    cars_number=models.CharField(max_length=100)

    class Meta:
        db_table = "bookinfouser"

class payment(models.Model):
    book_id=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)

    class Meta:
        db_table = "payment"

class paymentuser(models.Model):
    book_id=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)

    class Meta:
        db_table = "paymentuser"

class reviews(models.Model):
    advice=models.CharField(max_length=500)
    rating=models.IntegerField()

    class Meta:
        db_table = "feedback"
