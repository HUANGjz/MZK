from django.shortcuts import render
from django.http import HttpResponse
from callbook.models import *
from django.http import Http404

# Create your views here.
def home(request):
	post_list = CallBook.objects.all()
	event_list = EventCatalog.objects.all()
	singer_list = SingerCatalog.objects.all()
	second_list = SecondCatalog.objects.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
	return render(request,'home.html',dic)
	
def detail(request,id):
	try:
		temp = CallBook.objects.get(id = str(id)).name
	except CallBook.DoesNotExist:
		raise Http404
	try: 
		post_list = PicPath.objects.filter(name=temp)
	except PicPath.DoesNotExist:
		raise Http404
	event_list = EventCatalog.objects.all()
	singer_list = SingerCatalog.objects.all()
	second_list = SecondCatalog.objects.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
	return render(request,'post.html',dic)

def catalog(request,tag):
	try:
		temp_list = Tag.objects.filter(tag_name = tag) 
	except Tag.DoesNotExist:
		raise Http404
	callbook_list = CallBook.objects.all()
	post_list = []
	for cb in callbook_list:
		for temp in temp_list:
			if  temp.name == cb.name:
				post_list.append(cb)
	event_list = EventCatalog.objects.all()
	singer_list = SingerCatalog.objects.all()
	second_list = SecondCatalog.objects.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
	return render(request,'catalog.html',dic)

