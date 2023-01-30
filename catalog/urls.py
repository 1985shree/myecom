from django.urls import path
from .views import home, shop


urlpatterns = [
    path('', home, name = 'home'),
    path('', shop, name = 'shop')
]
