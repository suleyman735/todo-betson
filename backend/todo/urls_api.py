from django.urls import path

from . import views

from .views import UserListCreateView,ToDoItem,LoginUser


urlpatterns = [
    
     path('users/', UserListCreateView.as_view(), name='users'),
     path('todolist/', views.todo_list, name='todolist'),
    #  path('todocreate/', views.todo_create, name='todocreate'),
     path('login/', LoginUser.as_view(), name='api-login'),


   
]