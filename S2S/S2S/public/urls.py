from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [

	path('index', views.index, name='index'),
	path('search', views.search, name='search'),
	path('Register', views.Register, name='Register'),
	path('view_detail',views.view_detail, name= 'view_detail'),

	path('login', views.login, name='login'),
	path('signup', views.signup, name='signup'),
	

	path('Display', views.Display, name='Display'),

]