from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from rest_framework import permissions


@permission_classes((permissions.AllowAny,))
class OrderCreateView(APIView):
    """
    API endpoint that allows Orders to be created
    """
    def post(self, request):
        request_data = request.data.get('request')
        serializer = RequestsOrderSerializer(data=request_data)

        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()

        return JsonResponse({"success": "Order created successfully"})
