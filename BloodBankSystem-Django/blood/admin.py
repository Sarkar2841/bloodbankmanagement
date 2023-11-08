from django.contrib import admin

from blood.models import Stock
from blood.models import BloodRequest



# Register your models here.
admin.site.site_header="BLOOD BANK LORD | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display=['request_by_patient','request_by_donor','patient_name','patient_age','reason','bloodgroup','unit','status','date']
admin.site.register(BloodRequest,ContactAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['bloodgroup','unit']    
admin.site.register(Stock,ProductAdmin)


# Register your models here.
