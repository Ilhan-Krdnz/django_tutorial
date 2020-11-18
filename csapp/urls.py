from django.urls import path
from . import views

app_name = "csapp"
urlpatterns = [
	path('',views.index, name='index'),
	path('form/',views.form_ask,name='form_ask'),
	path('form_delete/',views.form_delete,name='form_delete'),
]
#path('<str:name>',views.greet, name='greet'),