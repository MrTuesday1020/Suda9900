from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
<<<<<<< HEAD
	path('', views.index, name='index'),
	path('Home', views.test, name='Home'),
	path('get_data', views.get_data, name='get_data'),
=======



	path('index', views.index, name='index'),
	path('search', views.search, name='search'),

	path('view_detail',views.view_detail, name= 'view_detail'),

	path('login', views.login, name='login'),
	path('signup', views.signup, name='signup'),
	





	path('login', views.login, name='login'),	# login page
	path('logout', views.logout, name='logout'),	# logout page
	path('signup', views.signup, name='signup'),	# signup page
	

	path('Home', views.Home, name='Home'),	# search house page
	path('Display', views.display, name='Display'),	# row houses page



	path('search', views.search, name='search'),	# search house page
	path('display', views.display, name='display'),	# row houses page
	path('view_detail', views.view_detail, name='view_detail'),	# house detial page

	path('index', views.index, name='index'),	# personal navs page
	path('profile', views.profile, name='profile'),	# personal profile page
	

>>>>>>> 14b13bb2bfa973718c4e64a8d2643c9209ad7ce9
]