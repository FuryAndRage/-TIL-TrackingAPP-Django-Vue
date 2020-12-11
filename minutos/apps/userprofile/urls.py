from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'userprofile'

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('myaccount/', views.my_account, name = 'myaccount'),
    path('logout/',views.logout, name = 'logout'),
    path('login/', views.login, name = 'login')
    #path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),

    #this logout view bellow it is a crap
    #path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]