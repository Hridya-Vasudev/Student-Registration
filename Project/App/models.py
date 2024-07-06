from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=100)
class Course(models.Model):
    name = models.CharField(max_length=100)
class WorkExperience(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enquiry_no = models.CharField(max_length=20)
    enquiry_date = models.DateField()
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    address = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=20)
    whatsapp_no = models.CharField(max_length=20)
    dob = models.DateField()
    has_work_experience = models.BooleanField()