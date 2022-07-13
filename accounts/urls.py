from django.urls import path
from .import views


app_name="accounts"

urlpatterns = [


    ###################  Website #######################
    # path('signup',views.signup,name="signup"),
    # path('home/',views.signup,name="signup"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('regpage/',views.regpage,name="regpage"),
    path('register/',views.register,name="register"),
    path('login_in/',views.login_in,name="login_in"),
   
   

]