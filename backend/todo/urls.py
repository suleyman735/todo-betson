
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('login/', views.login, name='login'),
     path('create/', views.create, name='create'),
     
     path('edit/<int:id>/', views.edit, name='edit'),
     path('update/<int:id>/', views.update, name='update'),
     path('delete/<int:id>', views.destroy, name='destroy'),
     
   
]
