"""rezal_prom_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from blocks import views as blockViews
from requests import views as requestViews

router = routers.DefaultRouter()
router.register(r'blocks/header', blockViews.HeaderBlockViewSet)
router.register(r'blocks/main', blockViews.MainBlockViewSet)
router.register(r'blocks/about', blockViews.AboutBlockViewSet)
router.register(r'blocks/warming', blockViews.WarmingBlockViewSet)
router.register(r'blocks/services', blockViews.ServicesBlockViewSet)
router.register(r'blocks/projects', blockViews.ProjectsBlockViewSet)
router.register(r'blocks/stages', blockViews.StagesBlockViewSet)
router.register(r'blocks/team', blockViews.TeamBlockViewSet)
router.register(r'blocks/questions', blockViews.QuestionsBlockViewSet)
router.register(r'blocks/reviews', blockViews.ReviewsBlockViewSet)
router.register(r'blocks/contacts', blockViews.ContactsBlockViewSet)
router.register(r'blocks/footer', blockViews.FooterBlockViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/send_request', requestViews.OrderCreateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

