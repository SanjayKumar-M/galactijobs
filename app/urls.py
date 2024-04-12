
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Indexpage,name="index"),
    path('signup/',views.Register,name="signup"),
    path('register/',views.RegisterUser,name="register")
]
