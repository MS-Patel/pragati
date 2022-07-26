from django.contrib import admin

# Register your models here.
from .models import Category,Service_types,Lead,Connector,Banner

# Register your models here.
admin.site.register(Category)
admin.site.register(Service_types)
admin.site.register(Lead)
admin.site.register(Connector)
admin.site.register(Banner)