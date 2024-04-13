from django.shortcuts import render,redirect
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

            return render(req, "app/otp.html",{'email':email})
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
            return render(req,"app/otp.html",{'email':email})
        
        
def OTP(req):
    return render(req,"app/otp.html")

def verifyOTP(req):
    email = req.POST['email']
    otp = req.POST['otp']
    user = Users.objects.get(email=email)
    
    if user:
        if user.otp == otp:
            return render(req,"app/login.html",{'msg':"OTP Verification Success"})
        else:
            return render(req,"app/otp.html",{'msg':"OTP Verification Failed"})
    else:
        return render(req,"app/signup.html",{'msg':"User not registered"})
   
    
def login(req):
    return render(req,"app/login.html")

from django.shortcuts import render, redirect

def loginUser(req):
    if req.method == 'POST':
        role = req.POST['role']
        if role == 'Candidate':
            email = req.POST['email']
            password = req.POST['password']
            try:
                user = Users.objects.get(email=email)
                if user.password == password and user.role == "Candidate":
                    candidate = Candidate.objects.get(user_id=user)
                    req.session['id'] = user.id
                    req.session['role'] = user.role
                    req.session['name'] = candidate.name
                    
                    return redirect('index')  # Redirect to the index page
                else:
                    return render(req, "app/login.html", {'msg': "Wrong Password"})
            except Users.DoesNotExist:
                return render(req, "app/login.html", {'msg': "User does not exist"})
        # Add similar logic for the 'Company' role
    return render(req, "app/login.html")  