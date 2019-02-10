from django.contrib.auth import get_user_model
User=get_user_model()

from django.shortcuts import render,redirect
from lists.models import Item,List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm,ExistingListItemForm

def home_page(request):
	return render(request, 'home.html',{'form':ItemForm()})
	
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


def new_list(request):
	form=ItemForm(data=request.POST)
	if form.is_valid():
		list_ = List.objects.create() 
		#Item(text=request.POST['text'], list=list_)
		list_.owner=request.user
		list_.save()
		form.save(for_list=list_)
		return redirect(list_)
	else:
		return render(request,'home.html',{'form':form})


def my_lists(request,email):
	owner=User.objects.get(email=email)
	return render(request,'my_lists.html',{'owner':owner})

