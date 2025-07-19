from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
     path('get-started/', views.get_started, name='get_started'), 
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('predict/', views.house_predict, name='predict'),
    
]
