from django.urls import path
from .views import GetUsers

urlpatterns =[
    path('users/<int:user_id>',GetUsers.as_view()), 
]