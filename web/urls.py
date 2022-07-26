from django.urls import path
from .import views


app_name="web"

urlpatterns = [


    ###################  Website Pages#######################
    path('',views.webhome,name="webhome"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('sentlead',views.sentlead,name="sentlead"),
    # path('get-topics-ajax/',views.get_topics_ajax, name="get_topics_ajax"),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),

  ###################  Web Contact Details #######################

    
    
    path('lead/view_webcontactdetails',views.view_webcontactdetails,name="view_webcontactdetails"),
    path('lead/add_webcontactdetails',views.add_webcontactdetails,name="add_webcontactdetails"),
    path('lead/create_webcontactdetails',views.create_webcontactdetails,name="create_webcontactdetails"),
    path('lead/edit_webcontactdetails/<int:id>',views.edit_webcontactdetails,name="edit_webcontactdetails"),
    path('lead/show_webcontactdetails/<int:id>',views.show_webcontactdetails,name="show_webcontactdetails"),
    path('lead/update_webcontactdetails<int:id>',views.update_webcontactdetails,name="update_webcontactdetails"),

]
