from django.contrib import admin

# Register your models here.

from .models import List,Item
'''
class ItemAdmin(admin.ModelAdmin):
	list_display=['text','list_id']
'''
class ItemInline(admin.StackedInline):
	model=Item

class ListAdmin(admin.ModelAdmin):
#	name=List.name
#	list_display=['name','owner']
	inlines=[ItemInline,]

	list_display = ['id']

'''
	def item_set(self, model_instance):
		return model_instance.item_set.all
'''
admin.site.register(List,ListAdmin)
