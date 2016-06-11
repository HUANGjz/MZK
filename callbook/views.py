from django.shortcuts import render
from django.http import HttpResponse
from callbook.models import *
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
	post_list = CallBook.objects.all()
	event_list = FirstCatalog.objects.filter(if_event=True)
	singer_list = FirstCatalog.objects.filter(if_event=False)
	second_list = SecondCatalog.objects.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
	return render(request,'home.html',dic)
	
def detail(request,id):
	try:
		temp = CallBook.objects.get(id = str(id))
	except CallBook.DoesNotExist:
		raise Http404
	try: 
		post_list = PicPath.objects.filter(name=temp)
	except PicPath.DoesNotExist:
		raise Http404
	event_list = FirstCatalog.objects.filter(if_event=True)
	singer_list = FirstCatalog.objects.filter(if_event=False)
	second_list = SecondCatalog.objects.all()
	tag_list = temp.tag_set.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list,'tag_list':tag_list}
	return render(request,'post.html',dic)

def catalog(request,id):
	try:
		post_list = Tag.objects.get(id = id).callbook.all()
	except Tag.DoesNotExist:
		raise Http404
	event_list = FirstCatalog.objects.filter(if_event=True)
	singer_list = FirstCatalog.objects.filter(if_event=False)
	second_list = SecondCatalog.objects.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
	return render(request,'catalog.html',dic)
	
@login_required	
def adminnew(request):
	return render(request,'adminnew.html')
	


