from django.db import models
from django.contrib.auth.models import User


class rooms(models.Model):
    room_no = models.IntegerField()
    date = models.DateField()
    price = models.FloatField()
    room_type = models.CharField(max_length=50)


class booking(models.Model):
    room_no = models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()
    amount=models.IntegerField()
    no_of_days=models.IntegerField()
    total_amount=models.IntegerField()
    u_id = models.IntegerField()
    date_now = models.DateTimeField(auto_now=True)
    no_bed = models.IntegerField(default=0)

class admin_table(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class payments(models.Model):
    name=models.CharField(max_length=100)
    card_no=models.CharField(max_length=100)
    month=models.IntegerField()
    year=models.IntegerField()
    cvv=models.IntegerField()

class phone(models.Model):
    phone=models.CharField(max_length=20)
    users=models.ForeignKey(User,on_delete=models.CASCADE)





