from django.contrib import admin
from .models import Student
from .models import Questions


# Register your models here.
admin.site.register(Student)
admin.site.register(Questions)