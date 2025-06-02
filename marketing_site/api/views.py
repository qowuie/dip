from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomUser
from orders.models import Order, Employee
from main.models import Service
from .serializers import UserSerializer, OrderSerializer, EmployeeSerializer, ServiceSerializer


# Получить всех пользователей
class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# Получить все заказы
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def get_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)


@api_view(['GET'])
def get_service(request, id_1c):
    try:
        service = Service.objects.get(id_1c=id_1c)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    except Service.DoesNotExist:
        return Response({'error': 'Service not found'}, status=404)


@api_view(['GET'])
def get_employee(request, id_1c):
    try:
        employee = Employee.objects.get(id_1c=id_1c)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)


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
        executor_id = request.data.get('id_1c')
        executor = Employee.objects.get(id_1c=executor_id)
        order.executor = executor
        order.save()
        return Response({'status': 'executor assigned'})
    except (Order.DoesNotExist, Employee.DoesNotExist):
        return Response({'error': 'Not found'}, status=404)


@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Удаление услуги по id_1c
@api_view(['DELETE'])
def delete_service(request, id_1c):
    try:
        service = Service.objects.get(id_1c=id_1c)
        service.delete()
        return Response({'status': 'service deleted'})
    except Service.DoesNotExist:
        return Response({'error': 'service not found'}, status=status.HTTP_404_NOT_FOUND)


# Удаление сотрудника по id_1c
@api_view(['DELETE'])
def delete_employee(request, id_1c):
    try:
        employee = Employee.objects.get(id_1c=id_1c)
        employee.delete()
        return Response({'status': 'employee deleted'})
    except Employee.DoesNotExist:
        return Response({'error': 'employee not found'}, status=status.HTTP_404_NOT_FOUND)
