from django.urls import path
from .views import home, records

urlpatterns = [
    path('', home, name='home'),
    path('records/', records, name='records'),
]
