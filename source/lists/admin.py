from django.contrib import admin

# Register your models here.

from .models import List,Item

class ItemAdmin(admin.ModelAdmin):
	list_display=['text','list']

class ListAdmin(admin.ModelAdmin):
	name=List.name
	list_display=['name','owner']
#	inlines=[ItemInline]


admin.site.register(List,ListAdmin)

admin.site.register(Item, ItemAdmin)
