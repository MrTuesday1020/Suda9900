from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('signup', views.signup, name='signup'),
	path('search', views.search, name='search'),
	path('book', views.book, name='book'),
	path('', views.adv_search, name='adv_search'),
	path('adv_search', views.adv_search, name='adv_search'),
	path('display', views.display, name='display'),
	path('view_detail/<int:id>', views.view_detail, name='view_detail'),
	path('profile', views.profile, name='profile'),
	path('upload_photo', views.upload_photo, name='upload_photo'),
	path('other_profile/<int:id>', views.other_profile, name='other_profile'),
]