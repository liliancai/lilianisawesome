from django.shortcuts import render,redirect
from lists.models import Item,List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm,ExistingListItemForm

def home_page(request):
	return render(request, 'home.html',{'form':ItemForm()})
'''
def view_list(request,list_id):
	list_=List.objects.get(id=list_id)
	error=None

	if request.method=='POST':
		try:
			item=Item.objects.create(text=request.POST['text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error="You can't have an empty list item"
	form=ItemForm()		
	return render(request, 'list.html', {
		'list': list_,'error':error,'form':form

	})
'''

def view_list(request,list_id):
	list_=List.objects.get(id=list_id)
	form=ExistingListItemForm(for_list=list_)
	if request.method=='POST':
		form=ExistingListItemForm(for_list=list_,data=request.POST)
		if form.is_valid():
			#Item.objects.create(text=request.POST['text'], list=list_)
			form.save()
			return redirect(list_)
	return render(request,'list.html',{'form':form,'list':list_})


	'''
#old models
#time to move on forms
def new_list(request):
	list_ = List.objects.create() 
	item=Item(text=request.POST['text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error="You can't have an empty list item"
		return render(request,'home.html',{'form':ItemForm(),'error':error})
		#it works!!!!
		#return render(request,'home.html',{'error':error})

	return redirect(list_)
'''
def new_list(request):
	form=ItemForm(data=request.POST)
	if form.is_valid():
		list_ = List.objects.create() 
		#Item(text=request.POST['text'], list=list_)
		form.save(for_list=list_)
		return redirect(list_)
	else:
		return render(request,'home.html',{'form':form})


