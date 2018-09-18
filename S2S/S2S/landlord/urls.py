from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'landlord'

urlpatterns = [
	path('add_house', views.add_house, name='add_house'),	# Add House
	path('manage_house', views.manage_house, name='manage_house'),	# Manage House
	path('add_house_pic', views.add_house_pic, name='add_house_pic'),
	path('edit_house', views.edit_house, name='edit_house'),
	path('history', views.history, name='history'),
	path('add_comm',views.add_comm,name='add_comm'),
]