from django.contrib import admin
from apps.accounts.models import User




class UserAdmin(admin.ModelAdmin):
    list_display=('email','username','gender','status','about',)
    list_filter = ("status",)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('gender','about')}),
        ('Permissions', {'fields': ('is_staff','is_active','is_superuser','status','date_joined',)}),
    )
    

admin.site.register(User,UserAdmin)
