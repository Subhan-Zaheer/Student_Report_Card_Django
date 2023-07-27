from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def get_students(request):
    students = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        students = Student.objects.filter(
            Q(student_name__icontains = search) |
            Q(department__department_name__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search),
        )
    p = Paginator(students, 5)
    page_number = request.GET.get('page')
    final_students_data = p.get_page(page_number)
    total_pages = p.num_pages
    data = {
        'final_data' : final_students_data,
        'last_page' : total_pages, 
        'page_list' : [i+1 for i in range(total_pages)]
    }
    return render(request, 'students.html', data)

def detailed_report_card(request, id):
    student = SubjectMarks.objects.filter(student__student_id__student_id = id)
    # total_subjects = student.subject.subject_name
    data = {
        'student' : student,
        # 'subjects' : total_subjects
    }
    return render(request, 'detailed_report.html', data)
