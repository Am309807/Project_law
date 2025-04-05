from rest_framework import serializers
from .models import ClientData

class ClientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientData
        fields = ['full_name', 'country', 'passport_no', 'phone_number', 'lost_company', 'lose_amount', 'lost_year']
