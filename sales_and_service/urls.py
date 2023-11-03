from django.urls import path
from sales_and_service import views

from . import views

urlpatterns = [
    path('profile/', views.profileList.as_view(), name='get_profiles_list'),
    path('profile/<pk>/', views.profileList.as_view(), name='get_profile_detail'),
]