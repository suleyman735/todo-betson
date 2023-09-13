from django import forms  
from .models import ToDoItem
class TodoForm(forms.ModelForm):  
    class Meta:
     model = ToDoItem
    #  fields=['title', 'description','created_date','due_date','done']
     fields = "__all__" 
     
    # title = forms.CharField(required=False,widget=forms.widgets.Input(
    #         attrs={
    #             "placeholder": "Ttile",
    #             "class": "form-control",
    #         }
    #     ),
    #     label="",
    # )
    # description=forms.CharField(required=False,widget=forms.widgets.Textarea(
    #         attrs={
    #             "placeholder": "Description",
    #             "class": "form-control",
    #         }
    #     ),
    #     label="",
    # )
    # created_date= forms.DateTimeField()
    # due_date= forms.TimeField()
    # done=forms.BooleanField()