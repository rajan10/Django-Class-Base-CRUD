from django.contrib import admin
from django.urls import path, include
from .views import HomeView,CreateStudentView, DetailStudentView,UpdateStudentView,DeleteStudentView

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('create_student/', CreateStudentView.as_view(), name="create_student"),
    path('detail_student/<int:pk>', DetailStudentView.as_view(), name="detail_student"),
    path('update_student/<int:pk>', UpdateStudentView.as_view(), name="update_student"),
    path('delete/<int:pk>', DeleteStudentView.as_view(), name="delete_student"),

]