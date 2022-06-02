from django import forms
from.import models
from django.db import models


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields =['college','first_name','last_name' ,'address','phone','parent_id' ,'email']