from django.contrib import admin

# Register your models here.

from .models import List,Item

class ListAdmin(admin.ModelAdmin):
#	list_display=['List().name']
	pass

admin.site.register(List,ListAdmin)

admin.site.register(Item)


