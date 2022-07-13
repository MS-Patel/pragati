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
]
