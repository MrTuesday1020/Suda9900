from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ['id','username']
	list_filter = ['username']
	search_fields = ['username']
	list_per_page = 10
	fields = ['username', 'first_name', 'last_name', 'password', 'phone', 'email', 'gender', 'dob', 'profile', 'activate', 'status', 'is_landlord']

class HouseAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	list_filter = ['name']
	search_fields = ['name']
	list_per_page = 10
	fieldsets = [
		('Basic Information', {'fields': ['user_id','name','address','postcode','price','profile']}),
		('House detail', {'fields': ['max_guests', 'no_of_beds','no_of_bedrooms','no_of_baths','no_of_parking'
									 ,'tv','kitchen','washer','fridge','conditioner','wifi','study_room',
									 'pool']}),
		('Extra Description', {'fields': ['house_rule','cancellation','extra','status']})
	]
class HousePicAdmin(admin.ModelAdmin):
	list_display = ['id','house_id']
	list_filter = ['house_id']
	search_fields = ['house_id']
	list_per_page = 10

class HouseRateAdmin(admin.ModelAdmin):
	list_display = ['id','house_id']
	list_filter = ['house_id']
	search_fields = ['house_id']
	list_per_page = 10

class LeasePeriodAdmin(admin.ModelAdmin):
	list_display = ['id','user_id','house_id','period_start','period_end']
	list_filter = ['user_id']
	search_fields = ['user_id']
	list_per_page = 10

class HouseCommentAdmin(admin.ModelAdmin):
	list_display = ['id','user_id','house_id']
	list_filter = ['user_id']
	search_fields = ['user_id']
	list_per_page = 10

class HouseTagAdmin(admin.ModelAdmin):
	list_display = ['id','house_id','tag_id']
	list_filter = ['house_id']
	search_fields = ['house_id']
	list_per_page = 10

class TagAdmin(admin.ModelAdmin):
	list_display = ['id','tag']
	list_filter = ['tag']
	search_fields = ['tag']
	list_per_page = 10

class UserTagAdmin(admin.ModelAdmin):
	list_display = ['id','user_id','tag_id']
	list_filter = ['user_id']
	search_fields = ['user_id']
	list_per_page = 10

admin.site.register(User,UserAdmin)
admin.site.register(House,HouseAdmin)
admin.site.register(House_Picture,HousePicAdmin)
admin.site.register(House_Rate,HouseRateAdmin)
admin.site.register(Lease_Period,LeasePeriodAdmin)
admin.site.register(House_Comment,HouseCommentAdmin)
admin.site.register(House_Tag,HouseTagAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(User_Tag,UserTagAdmin)


