from django.shortcuts import render
from random import randint
from .models import *

def Indexpage(req):
    return render(req, "app/index.html")

def Register(req):
    return render(req, "app/signup.html")

def RegisterUser(req):
    if req.POST['role'] == "Candidate":
        name = req.POST['name']
        contact = req.POST['contact']
        email = req.POST['email']
        password = req.POST['password']
        role = req.POST['role']

        user = Users.objects.filter(email=email)

        if user:
            message = "User already exists!"
            return render(req, "app/signup.html", {'msg': message})
        else:
            otp = randint(100000, 999999)

            newUser = Users.objects.create(role=role, otp=otp, email=email, password=password)
            newCandidate = Candidate.objects.create(user_id=newUser, name=name)

            return render(req, "app/otp.html")
    else:
        company_name = req.POST['name']
        contact = req.POST['contact']
        email = req.POST['email']
        password = req.POST['password']
        role = req.POST['role']
        
        company = Users.objects.filter(email=email)
        if(company):
            return render (req,"app/signup.html",{'msg':"Company already exists"})
        else:
            otp = randint(100000,999999)
            
            newUser = Users.objects.create(role=role,otp=otp,password=password)
            newCompany = Company.objects.create(user_id=newUser,company_name = company_name)
            return render(req,"app/otp.html")