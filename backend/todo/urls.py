
from django.urls import path
from . import views
from .views import UserListCreateView

urlpatterns = [
     path('', views.index, name='index'),
     # path('api/users/', UserListCreateView.as_view(), name='users'),

     path('signin/', views.signIn, name='signin'),
     path('logout_view/', views.logout_view, name='logout_view'),
     path('create/', views.create, name='create'),
     
     # path('edit/<int:id>/', views.edit, name='edit'),
     path('update/<int:id>/', views.update, name='update'),
     path('delete/<int:id>', views.destroy, name='destroy'),
     path('login/', views.loginIn, name='login'),
   
]
