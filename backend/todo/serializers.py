from rest_framework import serializers
from .models import UserCreating,ToDoItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreating
        fields = '__all__'
        
        

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreating
        fields = ('id', 'username', 'email')
        
        
class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id','title','description','created_date','due_date','done']
        
        def create(self,data):
            return ToDoItem.objects.create(**data)