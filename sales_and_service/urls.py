from django.urls import path
from sales_and_service import views

from . import views

urlpatterns = [
    path('profile/', views.profile_op.as_view(), name='get_profiles_list'),
    path('profile/<pk>/', views.profile_op.as_view(), name='get_profile_detail'),
    path('service/',views.service_op.as_view(), name='get_services_list'),
    path('service/<pk>/',views.service_op.as_view(), name='get_profile_services_list'),
    path('sales/',views.sales_op.as_view(), name='get_sales_list'),
    path('sales/<pk>/',views.sales_op.as_view(), name='get_profile_sales_list'),
]