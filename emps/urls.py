from django.urls import path
from .views import users


urlpatterns =[
    path('users/<int:user_id>',users,name='users'), 
    
]



# urlpatterns =[
#     path('users/<int:user_id>',GetUsers.as_view()), 
#     path('users1/',GetUsers1.as_view()),
# ]