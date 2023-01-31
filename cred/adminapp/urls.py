from django.urls import path
from . import views

urlpatterns = [
	path('',views.admin1, name = 'admin1'),
	path('owner/',views.owner, name = 'owner'),
	path('edit/',views.edit, name = 'edit'),
	path('update/<str:id>',views.update, name = 'update'),
	path('delete/<str:id>',views.delete, name = 'delete'),
	path("add",views.add, name = "add"),
	path("admin_logout",views.admin_logout, name = "admin_logout"),
]