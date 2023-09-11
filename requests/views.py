from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # Do not enforce CSRF checks



@permission_classes((permissions.AllowAny,))
class OrderCreateView(APIView):
    """
    API endpoint that allows Orders to be created
    """

    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        request_data = request.data.get('request')
        serializer = RequestsOrderSerializer(data=request_data)

        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()

            name = order_saved.name
            number = order_saved.number
            order_message = order_saved.message
            comfortable_time = order_saved.comfortable_time
            created = order_saved.created.strftime('%d-%m-%Y %H:%M:%S')

            subject = 'Новая заявка'
            plain_message = f"""Поступила новая заявка с сайта mebel-rezal.com
Имя: {name}
Номер телефона: {number}
Какая мебель нужна: {order_message}
Удобное время: {comfortable_time}
Создано: {created}

Пожалуйста, свяжитесь с клиентом в ближайшее время!

Для получения подробной информации проверьте панель администрирования."""

            html_message = f"""<html>
            <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                }}
                a {{
                    color: #2196F3;
                    text-decoration: none;
                }}
            </style>
            </head>
            <body>
            <p>Поступила новая заявка с сайта <a href="https://mebel-rezal.com" target="_blank">mebel-rezal.com</a></p>
            <p>Имя: {name}<br/>
            Номер телефона: {number}<br/>
            Какая мебель нужна: {order_message}<br/>
            Удобное время: {comfortable_time}<br/>
            Создано: {created}</p>
            <p>Пожалуйста, свяжитесь с клиентом в ближайшее время!</p>
            <p>Для получения подробной информации проверьте <a href="https://mebel-rezal.com/admin" target="_blank">панель администрирования</a>.</p>
            </body>
            </html>"""

            from_email = 'rezal.mebel@mail.ru'
            recipient_list = ['rezal.mebel@gmail.com']

            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

        return JsonResponse({"success": "Order created successfully"})
