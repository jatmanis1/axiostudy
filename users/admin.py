from django.contrib import admin

# Register your models here.
from users.models import Cust,Unit
class CustAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'mobile_no', 'email')

# admin.site.register(Cust, CustAdmin)

# class CustAdmin(admin.ModelAdmin):
#     list_display = ('username', 'name', 'mobile_no', 'email')

# admin.site.register(Cust, CustAdmin)

# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('username', 'name', 'mobile_no', 'email')

# admin.site.register(Cust, CustAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_desc','u_owner','u_link','u_course','u_part', 'u_subject')

admin.site.register(Cust, CustAdmin)
admin.site.register(Unit, UnitAdmin)