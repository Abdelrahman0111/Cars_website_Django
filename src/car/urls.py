from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('list', list, name='list'),
    path('add', add, name='add'),
    path('delete', delete, name='delete'),
]
