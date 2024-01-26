from django import forms
from .models import Task, TaskImage


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete']
        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'is_complete': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['is_complete'].widget.attrs.update({'class': ''})


class TaskImageForm(forms.ModelForm):
    class Meta:
        model = TaskImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(TaskImageForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({'class': 'form-control'})
