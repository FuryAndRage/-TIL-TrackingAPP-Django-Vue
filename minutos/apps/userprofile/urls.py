from django.urls import path
from . import views


app_name = 'userprofile'

urlpatterns = [
    
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('', views.my_account, name = 'myaccount'),
   
    #path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),

    #this logout view bellow it is a crap
    #path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]