from django.conf.urls import url
from django.urls import path
from BasicApp import views

app_name = "BasicApp"

urlpatterns = [
    # url(r"^relative/$", views.relative, name="relative"),
    # url(r"^other/$", views.other, name="other"),

    
    # path("relative/", views.relative, name="relative"),
    # path("other/", views.other, name="other"),
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
    
]
