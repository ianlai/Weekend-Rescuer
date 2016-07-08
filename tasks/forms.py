from django import forms

class AddTaskForm(forms.Form):
     input_title = forms.CharField(label='Title', max_length=100)
     input_detail = forms.CharField(label='Detail', max_length=500)


