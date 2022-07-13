from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name="lead"

urlpatterns = [


    ###################  Admin #######################
    path('home',views.home,name="home"),
    # path('lead/login',views.login,name="login"),
    # path('lead/registration',views.registration,name="registration"),
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

    ###################  Lead Details #######################
    path('lead/view_lead_reg',views.view_lead_reg,name="view_lead_reg"),
    path('lead/view_approved_lead_reg',views.view_approved_lead_reg,name="view_approved_lead_reg"),
    path('lead/view_pending_lead_reg',views.view_pending_lead_reg,name="view_pending_lead_reg"),
    path('lead/view_cancel_lead_reg',views.view_cancel_lead_reg,name="view_cancel_lead_reg"),
    path('lead/view_close_lead_reg',views.view_close_lead_reg,name="view_close_lead_reg"),
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

###################  Banner Details #######################

    
    
    path('lead/view_banner',views.view_banner,name="view_banner"),
    path('lead/add_banner',views.add_banner,name="add_banner"),
    path('lead/create_banner',views.create_banner,name="create_banner"),
    path('lead/edit_banner/<int:id>',views.edit_banner,name="edit_banner"),
    path('lead/show_banner/<int:id>',views.show_banner,name="show_banner"),
    path('lead/update_banner<int:id>',views.update_banner,name="update_banner"),

    ###################  Registration Details #######################
    path('lead/view_reg',views.view_reg,name="view_reg"),

]
