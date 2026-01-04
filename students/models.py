from django.db import models

#Models ==> module name
#Model helper class

class Students(models.Model):

    Gender_choices=[
        ('M', 'Male'),
        ('F', 'Female')
    ]

    roll_no=models.PositiveIntegerField(unique=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_no=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    year=models.PositiveIntegerField()
    dob=models.DateTimeField()
    gender=models.CharField(max_length=2, choices=Gender_choices)
    address=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True) #10:00
    updated_at=models.DateTimeField(auto_now=True) #11:00

    def __str__(self):
        return self.name


    # auto_now_add ==> stores the date & time when the record is created.
    # Value is set only once, never changes again.
    
    # auto_now ==> stores the date & time of the last update
    # updates every-time save() is called.

# Create your models here.


