from django.contrib import admin
from models import College
from models import School
from models import Events,Post



class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name','state','city')
    search_fields = ('name','state','city')
    list_filter = ('city','state')
admin.site.register(College, CollegeAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','state','city')
    search_fields = ('name','state','city')
    list_filter = ('city','state')
admin.site.register(School, SchoolAdmin)


class EventsAdmin(admin.ModelAdmin):
    list_display = ('name','state','city','startdate')
    search_fields = ('name','state','city')
    list_filter = ('city','state')
admin.site.register(Events, EventsAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('user','userName','date','college','collegeName','content','image')
    search_fields = ('userName','collegeName')
    list_filter = ('collegeName','flag')
admin.site.register(Post, PostAdmin)

