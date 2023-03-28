from rest_framework import serializers
from .models import *


class RequestsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('name',
                  'number',
                  'message',
                  'comfortable_time',
                  'project_version',
                  'user_agent',
                  'screen_resolution',
                  'browser_language',
                  'timezone',
                  'cookie')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
