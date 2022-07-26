from datetime import timezone

from django.db import models
from django.utils import timezone
# Create your models here.
class Webcontactdetails(models.Model):
    
    web_contactno=models.DecimalField(max_digits=10,decimal_places=0,default=0,null=True, blank=True)
    web_email=models.EmailField(max_length=254,null=True, blank=True)
    web_address=models.CharField(max_length=100,null=True, blank=True)
    web_worktime=models.CharField(max_length=50,null=True, blank=True)
   
    def __str__(self):
        return self.web_email