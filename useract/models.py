from django.db import models
from django.contrib.auth.models import User


class Authority(models.Model):
    authority_id = models.IntegerField(primary_key=True)
    authority_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10000)
    e_mail = models.EmailField()
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    authority_id = models.ForeignKey(
        Authority,
        null=False,
        on_delete=models.CASCADE)


class Inquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True)
    # dateTime= models.TimeField(auto_now_add=True)
    reported_date = models.CharField(max_length=20)
    reported_time = models.CharField(max_length=10)

    USERNAME = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,

    )
    description = models.CharField(max_length=1000)
    add_state = models.BooleanField()
    report_id = models.ForeignKey(

        Report,
        on_delete=models.CASCADE,
        null=False,

    )

class BusDetails(models.Model):
        bus_id = models.AutoField(primary_key=True)
        bus_no = models.CharField(max_length=10)
        route_no = models.IntegerField()
        start_destination = models.CharField(max_length=25)
        end_destination = models.CharField(max_length=25)
        type = models.CharField(max_length=10)

class TrainDetails(models.Model):
        train_id = models.AutoField(primary_key=True)
        train_name = models.CharField(max_length=100)
        route_no = models.IntegerField()
        strart_destination = models.CharField(max_length=25)
        end_destination = models.CharField(max_length=25)


class ProfilePic(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    picture = models.ImageField(upload_to='pictures',blank=True)

Users = (
    ('client','client'),
    ('admin', 'admin'),
    ('external','external'),
)

class UserType(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    type = models.CharField(max_length=10,choices=Users,default='client')

class AuthofUser(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    auth = models.ForeignKey(

        Authority,
        on_delete=models.CASCADE,
        null=False,
    )

