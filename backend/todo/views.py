from django.shortcuts import redirect, render
from .models import *

from .forms import TodoForm

# Create your views here.

def index(request):
    
    todoComplete = ToDoItem.objects.filter(done="True")
    todoRunning = ToDoItem.objects.filter(done="False")
   
    context = {'todoComplete': todoComplete,
               'todoRunning':todoRunning}
    return render(request, 'index.html',context)




def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        print(form)
        if form.is_valid():
            try:
    
                form.save()
      
            except:
                print('e')
    else:
        form = TodoForm()
    
    return render(request, 'create.html',{'form':form})


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
    return render(request, 'edit.html', {'todoEdit': todoEdit})

def destroy(request, id):  
    todoItem = ToDoItem.objects.get(id=id)  
    todoItem.delete()  
    return redirect("/")