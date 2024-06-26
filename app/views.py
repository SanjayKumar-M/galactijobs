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

def apply(req,pk):
    user = req.session['id']
    if user:
        cand = Candidate.objects.get(user_id = user)
        job = JobDetail.objects.get(id=pk)
    return render(req,"app/apply.html",{'user':user,'candidate':cand,'job':job})

def Applyjob(req, pk):
    user = req.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetail.objects.get(id=pk)

        if req.method == 'POST':
            name = req.POST['name']
            email = req.POST['email']
            contact = req.POST['contact']
            city = req.POST['city']
            state = req.POST['state']
            education = req.POST['education']
            experience = req.POST['experience']
            website = req.POST['website']
            gender = req.POST['gender']
            salary = req.POST['salary']
            resume = req.FILES['resume']

            # Update the candidate's profile information
            cand.name = name
            cand.email = email
            cand.contact = contact
            cand.city = city
            cand.state = state
            cand.education = education
            cand.experience = experience
            cand.website = website
            cand.gender = gender
            cand.salary = salary
            cand.save()

            # Create the application
            newapply = ApplyList.objects.create(
                candidate=cand,
                job=job,
                education=education,
                experience=experience,
                website=website,
                gender=gender,
                resume=resume,
                salary=salary
            )

            return render(req, "app/apply.html", {'msg': "Job applied successfully", 'candidate': cand, 'job': job})

    return render(req, "app/apply.html", {'candidate': cand, 'job': job})
    

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
        
def jobpost(req):
    return render(req,"app/company/jobpost.html")

def jobDetailsPost(req):
    if 'id' in req.session:  # Checking if 'id' is in the session data
        user_id = req.session['id']  # Accessing the user ID from the session
        user = Users.objects.get(id=user_id)  # Fetching the user object
        if user.role == "Company":
            company = Company.objects.get(user_id=user)
            jobname = req.POST['jobname']
            companyname = req.POST['companyname']
            companyaddress = req.POST['companyaddress']
            jobdescription = req.POST['jobdescription']
            qualification = req.POST['qualification']
            responsibility = req.POST['responsibility']
            location = req.POST['location']
            companywebsite = req.POST['companywebsite']
            companyemail = req.POST['companyemail']
            companycontact = req.POST['companycontact']
            salary = req.POST['salary']
            experience = req.POST['experience']
            logo = req.FILES['logo']
            
            job = JobDetail.objects.create(
                company_id=company,
                jobname=jobname,
                companyname=companyname,
                companyaddress=companyaddress,
                jobdescription=jobdescription,
                qualification=qualification,
                responsibility=responsibility,
                location=location, 
                companywebsite=companywebsite,
                companyemail=companyemail,
                companycontact=companycontact,
                salary=salary,
                experience=experience,
                logo=logo
            )
            return render(req, "app/company/jobpost.html", {'msg': "Job posted successfully!"})
   


def jobpostlist(req):
    alljob = JobDetail.objects.all()
    return render(req,"app/company/jobpostlist.html",{'alljob':alljob})

def candidatejobpostlist(req):
    alljob = JobDetail.objects.all()
    return render(req,"app/job-list.html",{'alljob':alljob})

def jobapplylist(req):
    all_jobapply =  ApplyList.objects.all()
    return render(req,"app/company/applyjoblist.html",{'all_job':all_jobapply})

def companylogout(req):
    del req.session['email']
    del req.session['password']
    return redirect('index')

