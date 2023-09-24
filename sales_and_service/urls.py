from django.urls import path
from sales_and_service import views

from . import views

urlpatterns = [
    path('profile/', views.profileList.as_view()),
    path('fetch_profile/<pk>/', views.ProfileDetail.as_view()),
]