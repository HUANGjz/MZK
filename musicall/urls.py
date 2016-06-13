"""musicall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^home/$','callbook.views.home',name='home'),
	url(r'^callbook_detail/(?P<id>\w+)/$', 'callbook.views.detail', name='detail'),
	url(r'^catalog/(?P<id1>\w+)/(?P<id2>\w+)/$', 'callbook.views.catalog', name='catalog'),
	url(r'^admin/new/$','callbook.views.adminnew',name='adminnew'),
	url(r'accounts/login/',login),
	url(r'^search/$','callbook.views.callbook_search',name='search'),
]


