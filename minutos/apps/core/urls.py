from django.urls import path
from . import views
from minutos.apps.userprofile import views as user_views

app_name = 'core'
urlpatterns = [
    path('', views.frontpage, name = 'frontpage'),
    path('privacypolicy/', views.privacy_policy, name = 'privacy'),
    path('termsofservice/', views.terms_of_service, name = 'terms'),
    path('plans/', views.plans, name = 'plans'),


    path('signup/', user_views.signup, name = 'signup'),
     path('logout/',user_views.logout, name = 'logout'),
    path('login/', user_views.login, name = 'login')
]