
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Indexpage, name="index"),
    path('signup/', views.Register, name="signup"),
    path('register/', views.RegisterUser, name="register"),
    path('verify-otp/', views.verifyOTP, name="verify-otp"),
    path('login/', views.loginUser, name="login"),
    path('profile/<int:pk>/',views.profile,name="profile"),
    path('updateprofile/<int:pk>/',views.updateProfile,name="updateprofile"),
    path('applyjob/<int:pk>',views.Applyjob,name="applyjob"),
    
    path('company/',views.companyIndex,name="company"),
    path('company-profile/<int:pk>',views.companyProfile,name="company-profile"),
    path('updatecompanyprofile/<int:pk>/',views.updateCompanyProfile,name="updatecompanyprofile"),
    path('jobpost/',views.jobpost,name="jobpostpage"),
    path('jobdetailpost/',views.jobDetailsPost,name="jobpost"),
    path('jobpostlist/',views.jobpostlist,name="jobpostlist"),
    path('apply/<int:pk>',views.apply,name = "apply"),
    
    path('joblist/',views.candidatejobpostlist,name="joblist"),
    path('companylogout/',views.companylogout,name="companylogout"),
    
        
    
]
