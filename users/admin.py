from django.contrib import admin

# Register your models here.
from users.models import Cust
class CustAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'mobile_no', 'email')

admin.site.register(Cust, CustAdmin)