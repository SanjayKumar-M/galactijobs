from django.db import models

class Users(models.Model):
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_updated = models.DateTimeField(auto_now_add=True)
    is_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Candidate(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.BigIntegerField(default=0)
    max_salary = models.BigIntegerField(default=0)
    jobtype = models.CharField(max_length=50,default='unknown')
    jobcategory = models.CharField(max_length=50,default='unknown')
    country = models.CharField(max_length=50, default='India')

    highest_education = models.CharField(max_length=50,default='unknown')
    experience = models.CharField(max_length=50,default='0')
    job_description = models.CharField(max_length=150,default='unknown')
    profile = models.ImageField(upload_to="app/img/candidates")
    def __str__(self):
        return self.name


class Company(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="app/img/companies")
    
    def __str__(self):
        return self.name