from django import forms  
class TodoForm(forms.Form):  
  title = forms.CharField(required=False,widget=forms.widgets.Input(
            attrs={
                "placeholder": "Ttile",
                "class": "form-control",
            }
        ),
        label="",
    )
  description=forms.CharField(required=False,widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "form-control",
            }
        ),
        label="",
    )