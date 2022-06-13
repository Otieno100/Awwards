from rest_framework import serializers
from .models import AwwardsMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwwardsMerch
        fields = ('name', 'description', 'price')