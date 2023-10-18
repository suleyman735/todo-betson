from django.db import IntegrityError
from django.shortcuts import redirect,get_object_or_404, render
from .models import *
from datetime import datetime



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
# def edit(request, id):
#     todoEdit = ToDoItem.objects.get(id=id)
#     return render(request,'edit.html', {'todoEdit':todoEdit})

def update(request, id):
    item = get_object_or_404(ToDoItem, pk=id)

    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        created_date = request.POST['created_date']
        # strDatetime = datetime.strptime(created_date,'%Y-%m-%dT%H:%M')
        due_date = request.POST['due_date']
        is_checked = request.POST.get('is_checked') == 'on'
        print(is_checked)
        item.title = title
        item.description = description
        item.created_date = created_date
        item.due_date = due_date
        item.done = is_checked
        item.save()

    return render(request, 'edit.html', {'todoEdit': item})


def destroy(request, id):  
    todoItem = ToDoItem.objects.get(id=id)  
    todoItem.delete()  
    return redirect("/")

def login(request):  
    # todoEdit = ToDoItem.objects.get(id=id)  
    return render(request,'login.html',) 