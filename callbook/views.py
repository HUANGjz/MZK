from django.shortcuts import render
from django.http import HttpResponse
from callbook.models import *
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
	posts = CallBook.objects.all()
	paginator = Paginator(posts,10)
	page = request.GET.get('page')
	try: 
		post_list = paginator.page(page)
	except PageNotAnInteger : 
		post_list = paginator.page(1)
	except EmptyPage :
		post_list = paginator.paginator(paginator.num_pages)
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

def catalog(request,id1,id2):
	try:
		post_list1 = Tag.objects.get(id = id1).callbook.all()
	except Tag.DoesNotExist:
		raise Http404
	if id2 == '0' :
		post_list2 = CallBook.objects.all()
	else :
		post_list2 = Tag.objects.get(id = id2).callbook.all()
	post_list = list(set(post_list1).intersection(set(post_list2)))
	event_list = FirstCatalog.objects.filter(if_event=True)
	singer_list = FirstCatalog.objects.filter(if_event=False)
	second_list = SecondCatalog.objects.all()
	dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
	return render(request,'catalog.html',dic)
	
@login_required	
def adminnew(request):
	return render(request,'adminnew.html')
	

def callbook_search(request):
	event_list = FirstCatalog.objects.filter(if_event=True)
	singer_list = FirstCatalog.objects.filter(if_event=False)
	second_list = SecondCatalog.objects.all()
	if 's' in request.GET:
		s = request.GET['s']
		if not s:
			post_list = CallBook.objects.all()
			dic = {'post_list':post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list}
			return render(request,'home.html',dic)
		else:
			temp_list = Tag.objects.filter(name__icontains = s)
			post_list=[]
			for temp in temp_list :
				post_list.extend(temp.callbook.all())
			post_list.extend(CallBook.objects.filter(name__icontains = s))
			post_list = list(set(post_list))
			if len(post_list) == 0 :
				return render(request,'archives.html', {'post_list' : post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list,'error' : True})
			else :
				return render(request,'archives.html', {'post_list' : post_list,'event_list':event_list,'singer_list':singer_list,'second_list':second_list,'error' : False})
	return redirect('/')
