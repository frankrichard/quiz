from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    no_of_attempts = models.IntegerField()
    total_marks = models.IntegerField()
    stu_question = models.CharField(max_length=100)
    youranswer = models.CharField(max_length=50)
    crctans = models.CharField(max_length=50)
    

class Questions(models.Model):
    questionno = models.IntegerField()
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    mark = models.IntegerField()
    
    
    