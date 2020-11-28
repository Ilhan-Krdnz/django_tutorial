from . import views
from django.urls import path

app_name = "user"

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('logout',views.logout_view,name="logout"),
]