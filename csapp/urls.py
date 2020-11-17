from django.urls import path
from . import views

app_name = "csapp"
urlpatterns = [
	path('',views.index, name='index'),
	path('form/',views.form_ask,name='form_ask'),
]
#path('<str:name>',views.greet, name='greet'),