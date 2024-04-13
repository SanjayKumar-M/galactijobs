
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Indexpage, name="index"),
    path('signup/', views.Register, name="signup"),
    path('register/', views.RegisterUser, name="register"),
    path('verify-otp/', views.verifyOTP, name="verify-otp"),
    path('login/', views.loginUser, name="login"),
    path('profile/<int:pk>/',views.profile,name="profile"),
    path('updateprofile/<int:pk>/',views.updateProfile,name="updateprofile")
    
]
