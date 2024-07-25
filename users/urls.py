from django.urls import path,re_path
from . import views
from django.contrib.auth.views import LoginView
app_name='users'
LoginView.template_name = 'users/login.html'
urlpatterns = [
    re_path(r'^login/$',LoginView.as_view(),name='login'),
    re_path(r'^logout/$',views.logout_view,name='logout'),
    re_path(r'^register/$',views.register,name="register"),
]
