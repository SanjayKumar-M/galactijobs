from django.shortcuts import render,redirect,get_object_or_404
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
            
            newUser = Users.objects.create(role=role,otp=otp,password=password,email=email)
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
        else:
            email = req.POST['email']
            password = req.POST['password']
            try:
                company = Users.objects.get(email=email)
                if company.password == password and company.role == "Company":
                    comp = Company.objects.get(user_id=company)
                    
                    req.session['id'] = company.id
                    req.session['role'] = company.role
                    req.session['name'] = comp.name
                    
                    return redirect('company')
                else:
                      return render(req, "app/login.html", {'msg': "Wrong Password"})
            except Users.DoesNotExist:
                return render(req, "app/login.html", {'msg': "User does not exist"})
                    
    return render(req, "app/login.html")  

def profile(request, pk):
    user = Users.objects.get(pk=pk)
    candidate = Candidate.objects.get(user_id=user)
    return render(request, "app/profile.html", {'user': user, 'candidate': candidate})

def updateProfile(req, pk):
    user = get_object_or_404(Users, pk=pk)
    
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.country = req.POST.get('country')
        can.city = req.POST.get('city')
        can.state = req.POST.get('state')
        can.dob = req.POST.get('dob')
        can.address = req.POST.get('address')
        can.gender = req.POST.get('gender')
        can.jobtype = req.POST.get('jobtype')
        can.jobcategory = req.POST.get('jobcategory')
        can.max_salary = req.POST.get('max_salary')
        can.min_salary = req.POST.get('min_salary')
        can.contact = req.POST.get('contact')
        can.highest_education = req.POST.get('highest_education')
        can.experience = req.POST.get('experience')
        can.job_description = req.POST.get('job_description')
        can.profile = req.POST.get('profile')
        can.save()
        return redirect('profile',pk=pk)
    return redirect('profile',pk=pk)

####################### COMPANY SIDE #############################

def companyIndex(req):
    return render(req,"app/company/index.html")

def companyProfile(req,pk):
     user = Users.objects.get(pk=pk)
     company = Company.objects.get(user_id=user)
     return render(req,"app/company/profile.html",{'user':user,'company':company})
 
def updateCompanyProfile(req,pk):
        user = get_object_or_404(Users, pk=pk)
        if user.role == "Company":
            company = Company.objects.get(user_id=user)
            company.name = req.POST.get('name')
            company.company_name = req.POST.get('company_name')
            company.city = req.POST.get('city')
            company.contact = req.POST.get('contact')
            company.address  = req.POST.get('address')
            company.state = req.POST.get('state')
            company.logo = req.POST.get('logo')
            company.save()
            return redirect('company-profile', pk=pk)   