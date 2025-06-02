from rest_framework import serializers
from accounts.models import CustomUser
from orders.models import Order
from orders.models import Employee
from main.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'category', 'price', 'id_1c']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'city', 'company', 'role']


class OrderSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    executor = UserSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'executor', 'service', 'wishes', 'contact_method', 'status', 'created_at']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id_1c', 'first_name', 'last_name', 'email', 'phone']
