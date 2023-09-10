from django.shortcuts import render

from .forms import TodoForm

# Create your views here.

def index(request):
    return render(request, 'index.html',)

def create(request):
     form=TodoForm
     if request.method == "POST":
         print('hellop')
         form = TodoForm(request.POST)
        #  print(form)
         if form.is_valid():
            
            cd = form.cleaned_data
            print(cd)
            form.save()
         else:
           form = TodoForm()
     return render(request, 'create.html',{'form':form})