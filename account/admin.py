from django.contrib import admin
from models import Users
# Register your models here
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phno','state','city')
    search_fields = ('name', 'email','phno')
    list_filter = ('city','state')
admin.site.register(Users, UsersAdmin)



