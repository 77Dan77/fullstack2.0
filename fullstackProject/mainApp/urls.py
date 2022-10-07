from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api import LeadViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/mainApp', LeadViewSet, 'mainApp')

urlpatterns = router.urls

# urlpatterns = [
#     path("", views.home),
#     path("create/", views.add_user),
#     path("edit/<int:id>/", views.update_user),
#     path("delete/<int:id>/", views.delete_user),
# ]
