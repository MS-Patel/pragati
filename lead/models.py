from datetime import timezone
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.

def con_doc_path(instance, filename):
    return 'connector_documents/{0}/{1}'.format(instance.con_code, filename)


class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Service_types(models.Model):
    category=models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
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
    lead_code=models.CharField(max_length=50,unique=True)
    lead_date=models.DateField(default=timezone.now)
    service_type=models.ForeignKey(Service_types,verbose_name="services",on_delete=models.CASCADE)
    party_name=models.CharField(max_length=50,null=True)  
    party_mobile=models.DecimalField(max_digits=10,decimal_places=0,null=True)
    party_email=models.EmailField(max_length=254,null=True)
    party_address=models.CharField(max_length=100,null=True)
    remark=models.CharField(max_length=250,null=True)
    connector=models.ForeignKey(Connector,verbose_name="connector",on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name