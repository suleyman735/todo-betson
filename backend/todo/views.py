from django.db import IntegrityError
from django.shortcuts import redirect,get_object_or_404, render
from django.contrib import messages
from .models import *
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework import status

from rest_framework import generics
from .serializers import UserSerializer,ToDoItemSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


# @login_required(login_url='/login/')
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserCreating.objects.all()
    serializer_class = UserSerializer
    
class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

# Todo GET view api  

@api_view(['GET','POST'])  
def todo_list(request):
    if request.method == 'GET':
        todolist = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(todolist,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


# @api_view(['POST'])  
# def todo_create(request):
#     serializer = ToDoItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    
    













# Create your views here.
def loginIn(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            print('Invalid credentials')
            return redirect('/login/')


    return render(request,'login.html')
    # print('jjj')
    # try:

        # if request.method == 'POST':
        #     username = request.POST['username']
        #     password = request.POST['password']
        #     print(username)
        #
        #     user = authenticate(username=username,password=password)
        #     print(user)
        #
        #     if user is not None:
        #         login(request,user)
        #         return redirect('/')
        # else:
        #         messages.info(request,'Invalid credentials')
        #         print('Invalid credentials')
        #         return redirect('/login/')

    # except IntegrityError as e:
    #      print(e)



def signIn(request):
    try:
        
        if request.method =="POST":
          
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=username,email=email,password=make_password(password))
            user.save()
            print(username,password)

            return redirect('login')
            
            
            
            print('post')
        
        
    except IntegrityError as e:
        print(e)
    # try:
    #     if request.method == "POST":
    #         username = request.POST['username']
    #         email = request.POST['email']
    #         password = request.POST['password']

    #         user = User.objects.create_user(id=id,username=username,email=email,password=make_password(password))
    #         user.save()
    #         print('hello bithch')
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,'User Taken')
    #             return redirect('signin/')
    #             print('Username taken')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(request, 'email taken')
    #             return redirect('signin/')
    #             print('email taken')
    #         else:
    #             return redirect('index/')
    #     else:
    #         return redirect('/')
    # except IntegrityError as e:
    #     print('e')
    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def index(request):
 
    todoComplete = ToDoItem.objects.filter(done="True",user=request.user)
    todoRunning = ToDoItem.objects.filter(done="False",user=request.user)

    context = {'todoComplete': todoComplete,
               'todoRunning':todoRunning}
    return render(request, 'index.html',context)


@login_required(login_url='/login/')
def create(request):
    try:
        if request.method =='POST':
            
            title = request.POST['title']
            description = request.POST['description']
            created_date = request.POST['created_date']
            # strDatetime = datetime.strptime(created_date,'%Y-%m-%dT%H:%M')
            due_date = request.POST['due_date']
            is_checked = request.POST.get('is_checked') == 'on'
            dataSave = ToDoItem(user= request.user, title=title, description=description, created_date=created_date, due_date=due_date, done=is_checked)
            dataSave.save()
            return render(request,'create.html')
    except IntegrityError as e:

        print('e')
    return render(request,'create.html')
# def edit(request, id):
#     todoEdit = ToDoItem.objects.get(id=id)
#     return render(request,'edit.html', {'todoEdit':todoEdit})
@login_required(login_url='/login/')
def update(request, id):
    item = get_object_or_404(ToDoItem, pk=id)

    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        created_date = request.POST['created_date']
        # strDatetime = datetime.strptime(created_date,'%Y-%m-%dT%H:%M')
        due_date = request.POST['due_date']
        is_checked = request.POST.get('is_checked')=='on'
        # print(is_checked)
        item.title = title
        item.description = description
        item.created_date = created_date
        item.due_date = due_date
        item.done = is_checked
        item.save()

    return render(request, 'edit.html', {'todoEdit': item})

@login_required(login_url='/login/')
def destroy(request, id):  
    todoItem = ToDoItem.objects.get(id=id)  
    todoItem.delete()  
    return redirect("/")

# def login(request):
#     # todoEdit = ToDoItem.objects.get(id=id)
#     return render(request,'login.html',)