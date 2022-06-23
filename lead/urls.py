from django.urls import path
from .import views

app_name="lead"

urlpatterns = [


    ###################  Website #######################
    path('',views.webhome,name="webhome"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    
    ###################  Admin #######################
    path('home',views.home,name="home"),
    path('lead/login',views.login,name="login"),
    path('lead/registration',views.registration,name="registration"),
    path('lead/report',views.report,name="report"),

    ###################  Category #######################
    
    path('lead/view_cat',views.view_cat,name="view_cat"),
    path('lead/add_cat',views.add_cat,name="add_cat"),
    path('lead/create_cat',views.create_cat,name="create_cat"),
    path('lead/edit_cat/<int:id>',views.edit_cat,name="edit_cat"),
    path('lead/update_cat/<int:id>',views.update_cat,name="update_cat"),
    
    
    ###################  Services #######################

    path('lead/view_ser_type',views.view_ser_type,name="view_ser_type"),
    path('lead/add_ser_type',views.add_ser_type,name="add_ser_type"),
    path('lead/create_ser_type',views.create_ser_type,name="create_ser_type"),
    path('lead/edit_ser_type/<int:id>',views.edit_ser_type,name="edit_ser_type"),
    path('lead/update_ser_type/<int:id>',views.update_ser_type,name="update_ser_type"),

    ###################  Party Details #######################

   
    path('lead/view_lead_reg',views.view_lead_reg,name="view_lead_reg"),
    path('lead/add_lead_reg',views.add_lead_reg,name="add_lead_reg"),
    path('lead/create_lead_reg',views.create_lead_reg,name="create_lead_reg"),
    path('lead/edit_lead_reg/<int:id>',views.edit_lead_reg,name="edit_lead_reg"),
    path('lead/update_lead_reg/<int:id>',views.update_lead_reg,name="update_lead_reg"),

    ###################  Connector Details #######################

    
    
    path('lead/view_con_reg',views.view_con_reg,name="view_con_reg"),
    path('lead/add_con_reg',views.add_con_reg,name="add_con_reg"),
    path('lead/create_con_reg',views.create_con_reg,name="create_con_reg"),
    path('lead/edit_con_reg/<int:id>',views.edit_con_reg,name="edit_con_reg"),
    path('lead/show_con_reg/<int:id>',views.show_con_reg,name="show_con_reg"),
    path('lead/update_con_reg<int:id>',views.update_con_reg,name="update_con_reg"),

]
