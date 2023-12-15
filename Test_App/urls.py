from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'invoice', HeaderViewSet, basename="invoice")

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
]
