from django.contrib import admin
from .models import wood_metal

# Register your models here
class woodprofileAdmin(admin.ModelAdmin):
    list_display=('id','name','description','furnature_image','updated')
  



admin.site.register(wood_metal,woodprofileAdmin)
admin.site.site_header='Duka Langu administration'
