from rest_framework import serializers
from accounts.models import CustomUser
from orders.models import Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'city', 'company', 'role']


class OrderSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    executor = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'executor', 'service', 'wishes', 'contact_method', 'status', 'created_at']
