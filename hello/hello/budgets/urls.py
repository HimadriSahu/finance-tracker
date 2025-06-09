from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
    # Add the individual user endpoint:
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
]