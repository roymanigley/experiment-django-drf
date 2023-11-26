from rest_framework import serializers

from accounting.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
