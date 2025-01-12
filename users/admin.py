from django.contrib import admin

# Register your models here.
from users.models import Unit, Subject,Course, UserProfile

# admin.site.register(Cust, CustAdmin)

# class CustAdmin(admin.ModelAdmin):
#     list_display = ('username', 'name', 'mobile_no', 'email')

# admin.site.register(Cust, CustAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified', 'mobile_no')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('s_name', 's_desc')
    
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_desc')

# admin.site.register(Cust, CustAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_desc','u_owner','u_link','u_course','u_part', 'u_subject')

# admin.site.register(Cust, CustAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserProfile, ProfileAdmin)