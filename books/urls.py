from django.urls import path, include
from books.views import index, create

urlpatterns = [
    path('', index, name='home'),
    path('create/', create, name='create'),
    
]