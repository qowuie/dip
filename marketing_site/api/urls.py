from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListAPIView.as_view(), name='user-list'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/status/', views.update_order_status, name='update-order-status'),
    path('orders/<int:pk>/assign/', views.assign_executor, name='assign-executor'),
    path('users/create/', views.create_user_from_1c, name='create-user-1c'),
]
