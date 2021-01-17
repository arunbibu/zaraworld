from django.db import models

# Create your models here.
class Parent(models.Model):
    FatherName= models.CharField(max_length=100,default="Father Name",blank=True)
    MotherName= models.CharField(max_length=100,default="Mother Name",blank=True)
    KidName= models.CharField(max_length=100,default="Kid Name",blank=True)
    Email= models.CharField(max_length=100,default="Email Address",blank=True)
    Password = models.CharField(max_length =100,default="Password",blank=True)
    Address = models.CharField(max_length =100,default="Address",blank=True)
    ProfileImage = models.FileField(blank=True)
    Age = models.CharField(max_length=100,default="0",blank=True)
    Phone = models.CharField(max_length=100,default="1234567890",blank=True)
    status = models.CharField(max_length=100,default="0",blank=True)
    attendance = models.CharField(max_length=100,default="0",blank=True)
    
    
class Staff(models.Model):
    StaffName = models.CharField(max_length=100,blank=True)
    Age = models.IntegerField()
    Address = models.CharField(max_length=100,default="example",blank=True)
    profileimage = models.FileField(blank=True,default='default.jpg')
    Phoneno = models.IntegerField(default=1,blank=True)
    Password = models.CharField(max_length=100, default="password",blank=True)
    Salary = models.IntegerField()
    Email = models.EmailField(default="123@123.com",blank=True)
    Status = models.IntegerField(default=0,blank=True)


class Admin(models.Model):

    Username = models.CharField(max_length=100,default="example",blank=True)
    profileimage = models.FileField(blank=True)
    Password = models.CharField(max_length=100, default="null",blank=True)
    Email = models.EmailField(default="123@123.com",blank=True)


class Attendance(models.Model):
    
    Name = models.CharField(max_length=100,default="sample",blank=True)
    Email = models.CharField(max_length=100,default="sample@sample.sample",blank=True)
    attendance = models.CharField(max_length=50,default="absent",blank=True)
    status = models.IntegerField(default=0)
    
    
class PhotoGallery(models.Model):
    Image = models.FileField(blank=True)
    
