from datetime import timezone
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.

def con_doc_path(instance, filename):
    return 'connector_documents/{0}/{1}'.format(instance.con_code, filename)

def banner_path(instance, filename):
    return 'webbanners/{0}/{1}'.format(instance.ban_code, filename)


class Category(models.Model): #country
    cat_id=models.CharField(max_length=100)
    name=models.CharField(max_length=100,unique=True)
    image=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service_types(models.Model): #city
    category=models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE, related_name='services')
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

class Connector(models.Model):
    con_code=models.CharField(max_length=50,unique=True)
    con_name=models.CharField(max_length=50)
    con_mobile=models.DecimalField(max_digits=10,decimal_places=0)
    con_email=models.EmailField(max_length=254)
    con_document=models.FileField(upload_to =con_doc_path, default='connector_documents/default.jpg')
    con_account_no=models.DecimalField(max_digits=20,decimal_places=0)
    con_ifsc_code=models.CharField(max_length=50)
    con_bank_name=models.CharField(max_length=50)
    con_branch=models.CharField(max_length=50)
    con_reg_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.con_name
    
class Lead(models.Model):
    STATUS = [
    
    ('PENDING', 'PENDING'),
    ('APPROVED', 'APPROVED'),
    ('CLOSE', 'CLOSE'),
    ('CANCEL', 'CANCEL'),
    ]
    lead_code=models.CharField(max_length=50,unique=True)
    lead_date=models.DateField(default=timezone.now)
    category=models.ForeignKey(Category,verbose_name="category",on_delete=models.CASCADE)
    service_type=models.ForeignKey(Service_types,verbose_name="services",on_delete=models.CASCADE)
    party_name=models.CharField(max_length=50,null=True, blank=True,)  
    party_mobile=models.DecimalField(max_digits=10,decimal_places=0,null=True ,blank=True,)
    party_email=models.EmailField(max_length=254,null=True, blank=True,)
    party_address=models.CharField(max_length=100,null=True, blank=True,)
    remark=models.CharField(max_length=250,null=True, blank=True,)
    connector=models.ForeignKey(Connector,verbose_name="connector",on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='PENDING', max_length=100)
    def __str__(self):
        return self.party_name


class Banner(models.Model):
    ban_code=models.CharField(max_length=50,unique=True)
    ban_img=models.FileField(upload_to =banner_path, default='webbanners/default.jpg')
    ban_comments=models.CharField(max_length=50)
    ban_update_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.ban_comments