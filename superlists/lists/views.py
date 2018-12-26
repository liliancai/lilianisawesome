'''0!=1 a new lists item have'nt be saved request.POST perhaps
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	if request.method == 'POST':
		return HttpResponse(request.POST['item_text']) 
	return render(request, 'home.html')
'''
from django.shortcuts import render,redirect
from lists.models import Item
'''
def home_page(request):
	item = Item()
	item.text = request.POST.get('item_text', '')
	item.save()
	return render(request, 'home.html',{
		#'new_item_text': request.POST.get('item_text', ''),
		'new_item_text': item.text
	})
def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text)
	else:
		new_item_text = ''
	return render(request, 'home.html', { 
		'new_item_text': new_item_text,
	})
'''
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text']) 
		return redirect('/')
	items = Item.objects.all()
	return render(request, 'home.html',{'items': items})