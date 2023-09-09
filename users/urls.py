from django.urls import path
from django.contrib.auth.views import LoginView
from . import views 
app_name = "users"


urlpatterns = [ 
    path(r'^login/', LoginView.as_view(template_name = 'login.html'),name = "login"),
    path(r'^logout/',views.logoutv,name = "logout"),
    path(r'^register/',views.register,name="register")
    ]