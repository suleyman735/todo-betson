from django.shortcuts import redirect, render
from .models import *

from .forms import TodoForm

# Create your views here.

def index(request):
    return render(request, 'index.html',)

def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                # cd = form.cleaned_data
                # print(cd)
                form.save()
                # return redirect("/create/")
            except:
                print('e')
    else:
        form = TodoForm()
    
    return render(request, 'create.html',{'form':form})