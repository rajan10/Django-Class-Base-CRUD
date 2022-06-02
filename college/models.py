from django.db import models

# Create your models here.
class College(models.Model):
    college_name=models.CharField(max_length=50)
    college_address=models.CharField(max_length=50)

    def __str__(self):
        return self.college_name


class Student(models.Model):
    college=models.ForeignKey(College, on_delete=models.CASCADE, related_name='colleges')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    parent_id=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering=['first_name']