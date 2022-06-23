import os
from django.shortcuts import render,redirect
from fileinput import filename
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from lead.models import Category, Connector, Lead, Service_types
from .forms import Category_form,Service_types_form,Connector_form,Lead_form


# Create your views here.
def webhome(request):
    return render(request,'webindex.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
  
def registration(request):
    return render(request,'register.html')

def report(request):
    return render(request,'report.html')
  

################## Category ######################

def view_cat(request):
    cat=Category.objects.all()
    return render(request,'view_cat.html',{'view_cat':cat})

def add_cat(request):
    cat=Category_form()
    return render(request,'add_cat.html',{'add_cat':cat})


def create_cat(request):

    if request.method == 'POST':
        
        name = request.POST.get("name")
        Category.objects.get_or_create(name=name)   

        return redirect('lead:view_cat')
     

def edit_cat(request,id):
    editcat=Category.objects.get(id=id)
    return render(request,'edit_cat.html',{'editcat':editcat})


def update_cat(request,id):
    if request.method == 'POST':

        name = request.POST.get("name")
        user=Category.objects.get(id=id)   
        user.name=name

        user.save()

        return redirect('lead:view_cat')

##################### service Type #######################

def view_ser_type(request):
    cat=Service_types.objects.all()
    return render(request,'view_ser_type.html',{'view_ser_type':cat})

def add_ser_type(request):
    cat=Service_types_form()
    category=Category.objects.all()
    return render(request,'add_ser_type.html',{'add_ser_type':cat,'category':category})


def create_ser_type(request):

    if request.method == 'POST':

        category = request.POST.get("category")
        cate = Category.objects.get(id=category)
        
        name = request.POST.get("name")
        Service_types.objects.get_or_create(name=name,category=cate)   

        return redirect('lead:view_ser_type')
     

def edit_ser_type(request,id):
    editsertype=Service_types.objects.get(id=id)
    return render(request,'edit_ser_type.html',{'editsertype':editsertype})


def update_ser_type(request,id):
    if request.method == 'POST':

        name = request.POST.get("name")
        user=Service_types.objects.get(id=id)   
        user.name=name

        user.save()

        return redirect('lead:view_ser_type')

##################### Lead #######################

def view_lead_reg(request):
    cat=Lead.objects.all()
    return render(request,'view_lead_reg.html',{'view_lead_reg':cat})

def add_lead_reg(request):
    cat=Lead_form()
    con=Lead.objects.all()
    connector = Lead.objects.last()
    if connector:
        no='LED/2223/' + str(int(connector.lead_code[9:]) + 1)
    else:
        no='LED/2223/1'
    service=Service_types.objects.all()
    connect=Connector.objects.all()
    return render(request,'add_lead_reg.html',{'add_lead_reg':cat,'in_num':no,'con':con,'connect':connect,'service':service})


def create_lead_reg(request):

    if request.method == 'POST':

        
        lead_code = request.POST.get("lead_code")

        service_type = request.POST.get("service_type")
        ser_type = Service_types.objects.get(id=service_type)

        party_name = request.POST.get("party_name")
        party_mobile = request.POST.get("party_mobile")
        party_email = request.POST.get("party_email")
        party_address = request.POST.get("party_address")
        remark = request.POST.get("remark")
    
        connector = request.POST.get("connector")
        conn = Connector.objects.get(id=connector)

        Lead.objects.get_or_create(lead_code=lead_code,party_name=party_name,party_mobile=party_mobile,party_email=party_email,party_address=party_address,remark=remark,service_type=ser_type,connector=conn)   

        return redirect('lead:view_lead_reg')
     

def edit_lead_reg(request,id):
    editleadreg=Lead.objects.get(id=id)
    ser_type = Service_types.objects.all()
    conn = Connector.objects.all()
    return render(request,'edit_lead_reg.html',{'editleadreg':editleadreg,'ser_type':ser_type,'conn':conn})


def update_lead_reg(request,id):
    if request.method == 'POST':

        lead_code = request.POST.get("lead_code")
        service_type = request.POST.get("service_type")
        ser_type = Service_types.objects.get(id=service_type)
        
        party_name = request.POST.get("party_name")
        party_mobile = request.POST.get("party_mobile")
        party_email = request.POST.get("party_email")
        party_address = request.POST.get("party_address")
        remark = request.POST.get("remark")
        connector = request.POST.get("connector")
        conn = Connector.objects.get(id=connector)

        user=Lead.objects.get(id=id) 
        user.service_type=ser_type
        user.connector=conn  
        user.lead_code=lead_code
        user.party_name=party_name
        user.party_mobile=party_mobile
        user.party_email=party_email
        user.party_address=party_address
        user.remark=remark
        
        user.save()

        return redirect('lead:view_lead_reg')

##################### Connector #######################

def view_con_reg(request):
    cat=Connector.objects.all()
    return render(request,'view_con_reg.html',{'view_con_reg':cat})

def add_con_reg(request):
    cat=Connector_form()
    con=Connector.objects.all()
    connector = Connector.objects.last()
    if connector:
        no='CON/2223/' + str(int(connector.con_code[9:]) + 1)
    else:
        no='CON/2223/1'
    return render(request,'add_con_reg.html',{'add_con_reg':cat,'in_num':no,'con':con})


def create_con_reg(request):

    if request.method == 'POST':

        
        con_code = request.POST.get("con_code")
        con_name = request.POST.get("con_name")
        con_mobile = request.POST.get("con_mobile")
        con_email = request.POST.get("con_email")
        con_document = request.FILES.get('con_document')
        con_account_no = request.POST.get("con_account_no")
        con_ifsc_code = request.POST.get("con_ifsc_code")
        con_bank_name = request.POST.get("con_bank_name")
        con_branch = request.POST.get("con_branch")


        Connector.objects.get_or_create(con_code=con_code,con_name=con_name,con_mobile=con_mobile,con_email=con_email,con_document=con_document,con_account_no=con_account_no,con_ifsc_code=con_ifsc_code,con_bank_name=con_bank_name,con_branch=con_branch)   
        
        return redirect('lead:view_con_reg')
     

def edit_con_reg(request,id):
    editconreg=Connector.objects.get(id=id)
    return render(request,'edit_con_reg.html',{'editconreg':editconreg})

def show_con_reg(request,id):
    editconreg=Connector.objects.get(id=id)
    return render(request,'show_con_reg.html',{'editconreg':editconreg})


def update_con_reg(request,id):
    user=Connector.objects.get(id=id)   

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(user.con_document) > 0:
                os.remove(user.con_document.path)
            user.con_document=request.FILES['con_document']
        user.con_code = request.POST.get("con_code")
        user.con_name = request.POST.get("con_name")
        user.con_mobile = request.POST.get("con_mobile")
        user.con_email = request.POST.get("con_email")


        # con_document = request.FILES.get('con_document')
        user.con_account_no = request.POST.get("con_account_no")
        user.con_ifsc_code = request.POST.get("con_ifsc_code")
        user.con_bank_name = request.POST.get("con_bank_name")    
        user.con_branch = request.POST.get("con_branch")

        user.save()
        messages.success(request, "documents update")
        return redirect('lead:view_con_reg')

    context = {'user':user}
    return render(request,'edit_con_reg.html',context)