from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic
from college.models import Student, College
from django.urls import reverse

# student
class HomeView(generic.ListView):
    template_name='college/index.html'
    model=Student

class CreateStudentView(generic.CreateView):
    model=Student
    template_name='college/create_student.html'
    fields=['college','first_name','last_name','address','phone','parent_id','email']

    def get_success_url(self):
        return reverse('index')

class DetailStudentView(generic.DetailView):
    model=Student
    template_name = 'college/detail_student.html'

class UpdateStudentView(generic.UpdateView):
    model=Student
    template_name='college/update_student.html'
    fields=['college','first_name','last_name','address','phone','parent_id','email']

    def get_success_url(self):
        return reverse('index')

class DeleteStudentView(generic.DeleteView):
    model=Student
    template_name = 'college/delete_student.html'

    def get_success_url(self):
        return reverse('index')

