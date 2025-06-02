from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListAPIView.as_view(), name='user-list'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/status/', views.update_order_status, name='update-order-status'),
    path('orders/<int:pk>/assign/', views.assign_executor, name='assign-executor'),
    path('orders/<int:pk>/', views.get_order, name='get-order-by-id'),
    path('services/<str:id_1c>/', views.get_service, name='get-service-by-id_1c'),
    path('employees/<str:id_1c>/', views.get_employee, name='get-employee-by-id_1c'),
    path('employees/', views.create_employee, name='create_employee'),
    path('services/', views.create_service, name='create_service'),
    path('services/<str:id_1c>/delete/', views.delete_service, name='delete_service'),
    path('employees/<str:id_1c>/delete/', views.delete_employee, name='delete_employee'),
]
