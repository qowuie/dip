from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomUser
from orders.models import Order
from .serializers import UserSerializer, OrderSerializer


# Получить всех пользователей


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# Получить все заказы


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Обновить статус заказа
@api_view(['PATCH'])
def update_order_status(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        order.status = request.data.get('status', order.status)
        order.save()
        return Response({'status': 'updated'})
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)


# Назначить исполнителя
@api_view(['PATCH'])
def assign_executor(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        executor_id = request.data.get('executor_id')
        executor = CustomUser.objects.get(pk=executor_id)
        if executor.role != 'employee':
            return Response({'error': 'User is not an employee'}, status=400)
        order.executor = executor
        order.status = 'in_progress'
        order.save()
        return Response({'status': 'executor assigned'})
    except (Order.DoesNotExist, CustomUser.DoesNotExist):
        return Response({'error': 'Not found'}, status=404)


# Создание сотрудника/админа
@api_view(['POST'])
def create_user_from_1c(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
