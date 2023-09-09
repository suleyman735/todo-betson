from django.shortcuts import render

from .forms import TodoForm

# Create your views here.

def index(request):
    return render(request, 'index.html',)

def create(request):
     if request.method == "POST":
         print('hellop')
         form = (request.POST)
         if form.is_valid():
            form.save()
         else:
           form = TodoForm()
     return render(request, 'create.html',{'form':TodoForm})