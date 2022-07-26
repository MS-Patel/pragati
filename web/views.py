from cProfile import label
from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.http import JsonResponse

import json as simplejson
from lead.models import Banner,Category, Connector, Lead, Service_types
from django.contrib import messages

from web.models import Webcontactdetails

# Create your views here.
# Create your views here.
def webhome(request):
    cat= Category.objects.all().order_by('cat_id')[:4]
    service=Service_types.objects.all()
    service_count=service.count()
    banner= Banner.objects.all()    
    webcontactdetails=Webcontactdetails.objects.all()
    return render(request,'website/webindex.html',{'cat':cat,'service_count':service_count,'banner':banner,'webcontactdetails':webcontactdetails})

def about(request):
    cat=Category.objects.all().order_by('cat_id')[:4]
    return render(request,'website/about.html',{'cat':cat})

def services(request):
    cat=Category.objects.all()
    return render(request,'website/services.html',{'cat':cat})

def contact(request):
    cat= Category.objects.all().order_by('cat_id')[:4]
    category=Category.objects.all()
    print(category)
   
    con=Lead.objects.all()
    connector = Lead.objects.last()
    if connector:
        no='LED/2223/' + str(int(connector.lead_code[9:]) + 1)
    else:
        no='LED/2223/1'
    # service=Service_types.objects.all()
    connect=Connector.objects.all()
    webcontactdetails=Webcontactdetails.objects.all()
    return render(request,'website/contact.html',{'webcontactdetails':webcontactdetails,'in_num':no,'con':con,'connect':connect,'category':category,'cat':cat})

def load_states(request):
    category_id = request.GET.get('category')
   
    services = Service_types.objects.filter(category_id=category_id).order_by('name')
    
    return render(request, 'drop_services.html', {'services': services})



def sentlead(request):
    
    if request.method == 'POST':
        print(request.POST)
        
        lead_code = request.POST.get("lead_code")

        if request.POST.get("category"):
            category = Category.objects.get(id=request.POST.get("category"))
        else:
            return HttpResponse("please enter category")



        if request.POST.get("service_type"):
            service_type = Service_types.objects.get(id=request.POST.get("service_type"))
        else:
            return HttpResponse("please enter category")
        


        # service_type = request.POST.get("service_type")
        # ser_type = Service_types.objects.get(id=service_type)
        party_name = request.POST.get("party_name")
        party_mobile = request.POST.get("party_mobile")
        party_email = request.POST.get("party_email")
        remark = request.POST.get("remark")

        conn = Connector.objects.get(con_name=str(request.user))
        
        Lead.objects.get_or_create(category=category,service_type=service_type,lead_code=lead_code,party_name=party_name,party_mobile=party_mobile,party_email=party_email,remark=remark,connector=conn)   
        messages.success(request, 'Thank You ! We Contact You soon.')
        return redirect('web:contact')

    
 ######################## Website Contact Details ############################

def view_webcontactdetails(request):
    webcontactdetails=Webcontactdetails.objects.all()
    return render(request,'view_webcontactdetails.html',{'view_webcontactdetails':webcontactdetails})

def add_webcontactdetails(request):
    
    webcontactdetails=Webcontactdetails.objects.all()
   
    return render(request,'add_webcontactdetails.html',{'add_webcontactdetails':webcontactdetails})


def create_webcontactdetails(request):

    if request.method == 'POST':

        
        web_contactno = request.POST.get("web_contactno")
        web_email = request.POST.get("web_email")
        web_address = request.POST.get("web_address")
        web_worktime = request.POST.get("web_worktime")
     
       

        Webcontactdetails.objects.get_or_create(web_contactno=web_contactno,web_email=web_email,web_address=web_address,web_worktime=web_worktime)   
        
        return redirect('web:view_webcontactdetails')
     

def edit_webcontactdetails(request,id):
    editwebcontactdetails=Webcontactdetails.objects.get(id=id)
    return render(request,'edit_webcontactdetails.html',{'editwebcontactdetails':editwebcontactdetails})

def show_webcontactdetails(request,id):
    editwebcontactdetails=Webcontactdetails.objects.get(id=id)
    return render(request,'show_webcontactdetails.html',{'editwebcontactdetails':editwebcontactdetails})


def update_webcontactdetails(request,id):
    user=Webcontactdetails.objects.get(id=id)   

    if request.method == 'POST':
        
       
        user.web_contactno = request.POST.get("web_contactno")
        user.web_email = request.POST.get("web_email")
        user.web_address = request.POST.get("web_address")
        user.web_worktime = request.POST.get("web_worktime")

        user.save()
        # messages.success(request, "Banner update")
        return redirect('web:view_webcontactdetails')

    context = {'user':user}
    return render(request,'edit_webcontactdetails.html',context)          