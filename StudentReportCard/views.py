from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def get_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'data' : students})
