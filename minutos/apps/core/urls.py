from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.frontpage, name = 'frontpage'),
    path('privacypolicy/', views.privacy_policy, name = 'privacy'),
    path('termsofservice/', views.terms_of_service, name = 'terms'),
    path('plans/', views.plans, name = 'plans'),
]