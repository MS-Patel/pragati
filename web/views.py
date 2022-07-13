from cProfile import label
from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json as simplejson
from lead.models import Banner, Category, Connector, Lead, Service_types
from django.contrib import messages

# Create your views here.
# Create your views here.

def webhome(request):
    cat= Category.objects.all().order_by('cat_id')[:4]
    service=Service_types.objects.all()
    service_count=service.count()
    banner= Banner.objects.all()

    return render(request,'website/webindex.html',{'cat':cat,'service_count':service_count,'banner':banner})

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
    return render(request,'website/contact.html',{'in_num':no,'con':con,'connect':connect,'category':category,'cat':cat})

def load_states(request):
    category_id = request.GET.get('category')
   
    services = Service_types.objects.filter(category_id=category_id).order_by('name')
    
    return render(request, 'drop_services.html', {'services': services})


# def get_topics_ajax(request):
#     if request.method == "POST":
#         cat_id = request.POST['cat_id']
#         try:
#             category = Category.objects.filter(id = cat_id).first()
#             topics = Service_types.objects.filter(category = category)
#         except Exception:
#             data['error_message'] = 'error'
#             return JsonResponse(data)
#         return JsonResponse(list(topics.values('id', 'name')), safe = False) 

def sentlead(request):
    
    if request.method == 'POST':
        print(request.POST)
        
        lead_code = request.POST.get("lead_code")

        if request.POST.get("category"):
            category = Category.objects.get(id=request.POST.get("category"))
        else:
            return HttpResponse("please enter category")


        # service_type = request.POST.get("service_types")
        # ser_type = Service_types.objects.get(id=service_type)

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

    
        