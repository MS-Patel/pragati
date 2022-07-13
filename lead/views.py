import os
from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.models import Register
from lead.models import Banner, Category, Connector, Lead, Service_types
from .forms import Banner_form, Category_form,Service_types_form,Connector_form,Lead_form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count



def home(request):
    service=Service_types.objects.all()
    service_count=service.count()

    lead=Lead.objects.all()
    lead_count=lead.count()
   
    today_lead= Lead.objects.values('lead_date').annotate(count=Count('lead_date')).values('count').order_by('lead_date').last()

    pending_leads=Lead.objects.filter(status='PENDING').count()

   

    connector=Connector.objects.all()
    connector_count=connector.count()


    
   
    chart_lead= Lead.objects.filter(status='PENDING').count()
    chart_completed_lead= Lead.objects.filter(status='APPROVED').count()
    chart_close_lead= Lead.objects.filter(status='CLOSE').count()
    chart_cancel_lead= Lead.objects.filter(status='CANCEL').count()

   


    return render(request,'index.html',{'chart_close_lead':chart_close_lead,'chart_cancel_lead':chart_cancel_lead,'chart_lead':chart_lead,'chart_completed_lead':chart_completed_lead,'pending_leads':pending_leads,'today_lead':today_lead,'service_count':service_count,'lead_count':lead_count,'lead':lead,'connector_count':connector_count})

# def login(request):
#     return render(request,'login.html')
  
# def registration(request):
#     return render(request,'register.html')




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
    
    cat= Lead.objects.all()
    return render(request,'view_lead_reg.html',{'view_lead_reg':cat})

def view_pending_lead_reg(request):
    
    cat= Lead.objects.filter(status='PENDING')
    return render(request,'view_lead_reg.html',{'view_lead_reg':cat})

def view_approved_lead_reg(request):
    
    cat= Lead.objects.filter(status='APPROVED')
    return render(request,'view_lead_reg.html',{'view_lead_reg':cat})

def view_close_lead_reg(request):
    
    cat= Lead.objects.filter(status='CLOSE')
    return render(request,'view_lead_reg.html',{'view_lead_reg':cat})

def view_cancel_lead_reg(request):
    
    cat= Lead.objects.filter(status='CANCEL')
    return render(request,'view_lead_reg.html',{'view_lead_reg':cat})

def add_lead_reg(request):
    category=Category.objects.all()
    cat=Lead_form()
    con=Lead.objects.all()
    connector = Lead.objects.last()
    if connector:
        no='LED/2223/' + str(int(connector.lead_code[9:]) + 1)
    else:
        no='LED/2223/1'
   # service=Service_types.objects.all()
    connect=Connector.objects.all()
    return render(request,'add_lead_reg.html',{'add_lead_reg':cat,'in_num':no,'con':con,'connect':connect,'category':category})


def create_lead_reg(request):

    if request.method == 'POST':

        
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
        party_address = request.POST.get("party_address")
        remark = request.POST.get("remark")
    
        #connector = request.POST.get("connector")
        conn = Connector.objects.get(id=1)

        Lead.objects.get_or_create(category=category,service_type=service_type,lead_code=lead_code,party_name=party_name,party_mobile=party_mobile,party_email=party_email,party_address=party_address,remark=remark,connector=conn)   
        messages.success(request, 'Thank You !Your Lead Save Successfully........')
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


################### Registrartion Details #######################
def view_reg(request):
    cat=Register.objects.all()
    return render(request,'view_reg.html',{'view_reg':cat})

######################## Banners Update ############################

def view_banner(request):
    banner=Banner.objects.all()
    return render(request,'view_banner.html',{'view_banner':banner})

def add_banner(request):
    category=Category.objects.all()
    ban=Banner_form()
    banne=Banner.objects.all()
    connector = Banner.objects.last()
    if connector:
        no='BAN/2223/' + str(int(connector.ban_code[9:]) + 1)
    else:
        no='BAN/2223/1'
    connect=Connector.objects.all()
    return render(request,'add_banner.html',{'add_banner':ban,'in_num':no,'banne':banne,'connect':connect,'category':category})


def create_banner(request):

    if request.method == 'POST':

        
        ban_code = request.POST.get("ban_code")
        
        ban_img = request.FILES.get('ban_img')
        ban_comments = request.POST.get("ban_comments")
        


        Banner.objects.get_or_create(ban_code=ban_code,ban_img=ban_img,ban_comments=ban_comments)   
        
        return redirect('lead:view_banner')
     

def edit_banner(request,id):
    editbanner=Banner.objects.get(id=id)
    return render(request,'edit_banner.html',{'editbanner':editbanner})

def show_banner(request,id):
    editbanner=Banner.objects.get(id=id)
    return render(request,'show_banner.html',{'editbanner':editbanner})


def update_banner(request,id):
    user=Banner.objects.get(id=id)   

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(user.ban_img) > 0:
                os.remove(user.ban_img.path)
            user.ban_img=request.FILES['ban_img']
        user.ban_code = request.POST.get("ban_code")
        user.ban_comments = request.POST.get("ban_comments")
       

        user.save()
        # messages.success(request, "Banner update")
        return redirect('lead:view_banner')

    context = {'user':user}
    return render(request,'edit_banner.html',context)    


