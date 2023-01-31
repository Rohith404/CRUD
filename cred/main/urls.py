from django.urls import path
from . import views

urlpatterns = [
	path('',views.user_login, name = "user_login"),
	path("user_logout",views.user_logout, name = "user_logout"),
	path("register",views.register, name = "register"),
	path("home",views.home, name = "home"),
	path('edit/',views.edit, name = 'edit'),
	path('update/<str:id>',views.update, name = 'update'),
	path('delete/<str:id>',views.delete, name = 'delete'),
	path("add",views.add, name = "add"),
	path("admin_logout",views.admin_logout, name = "admin_logout"),
	
]