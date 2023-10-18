from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import *
from datetime import datetime

from .forms import TodoForm

# Create your views here.

def index(request):
    
    todoComplete = ToDoItem.objects.filter(done="True")
    todoRunning = ToDoItem.objects.filter(done="False")
   
    context = {'todoComplete': todoComplete,
               'todoRunning':todoRunning}
    return render(request, 'index.html',context)

def create(request):
    try:
        if request.method =='POST':
            title = request.POST['title']
            description = request.POST['description']
            created_date = request.POST['created_date']
            # strDatetime = datetime.strptime(created_date,'%Y-%m-%dT%H:%M')
            due_date = request.POST['due_date']
            is_checked = request.POST.get('is_checked')=='on'
            dataSave = ToDoItem(title=title, description=description, created_date=created_date, due_date=due_date, done=is_checked)
            dataSave.save()
            return render(request,'create.html')
    except IntegrityError as e:

        print(e)
    return render(request,'create.html')
def edit(request, id):  
    todoEdit = ToDoItem.objects.get(id=id)  
    return render(request,'edit.html', {'todoEdit':todoEdit}) 

def update(request, roll): 
    # title = request.POST.get('title')
    # description = request.POST.get('description')
    # created_date = request.POST.get('created_date')
    # due_date = request.POST.get('due_date')
    # done = request.POST.get('done')
    
    # std= ToDoItem.objects.get(pk=roll)
    
    # std.title=title
    # std.description = description
    # std.created_date = created_date
    # std.due_date = due_date
    # std.done= done
    
    # std.save()
    # print('hello') 
    todoEdit = ToDoItem.objects.get(id=id)  
    form = TodoForm(request.POST, instance = todoEdit)  
        
    if form.is_valid():  
        form.save() 
        print(form) 
        return redirect("/") 
    else:
        print(form.errors) 
    return render(request, 'edit.html', {'todoEdit': todoEdit})

def destroy(request, id):  
    todoItem = ToDoItem.objects.get(id=id)  
    todoItem.delete()  
    return redirect("/")

def login(request):  
    # todoEdit = ToDoItem.objects.get(id=id)  
    return render(request,'login.html',) 