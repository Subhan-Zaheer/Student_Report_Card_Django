from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import *

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
        return render(request, 'students.html', {'final_data' : students})
    p = Paginator(students, 10)
    page_number = request.GET.get('page')
    final_students_data = p.get_page(page_number)
    total_pages = p.num_pages
    data = {
        'final_data' : final_students_data,
        'last_page' : total_pages, 
        'page_list' : [i+1 for i in range(total_pages)]
    }
    return render(request, 'students.html', data)

def calculating_grades(percentage):
    if percentage >=95:
        return "A+"
    elif percentage >= 85 and percentage < 95:
        return "A"
    elif percentage >= 75 and percentage < 85:
        return "B+"
    elif percentage >= 65 and percentage < 75:
        return "B"
    elif percentage >= 55 and percentage < 65:
        return "C+"
    elif percentage >= 45 and percentage < 55:
        return "C"
    elif percentage >= 33 and percentage < 45:
        return "D"
    else:
        return "F"
    pass

def detailed_report_card(request, id):
    studentmarks = SubjectMarks.objects.filter(student__student_id__student_id = id)
    student = Student.objects.filter(student_id__student_id = id)
    obtained_marks = int(studentmarks.aggregate(Sum('marks'))['marks__sum']) # It will return a key/value pair. 
    # That's why we have to subscript the dict to get the actual value.

    percentage = round((obtained_marks/400) * 100, 3) # Rounding off the value of percentage upto 3 decimal places.
    grade = calculating_grades(percentage)
    rank = Student_Rank.objects.filter(student__student_id__student_id = id)
    student_rank = 0
    date_of_generation = None
    for _ in rank:
        student_rank = _.student_rank
        date_of_generation = _.date_of_generating_report
    data = {
        'studentmarks' : studentmarks,
        'mystudent' : student,
        'obtainedmarks' : obtained_marks,
        'percentage' : percentage,
        'grade' : grade,
        'rank' : student_rank,
        'date_of_generation' : date_of_generation,
    }
    return render(request, 'detailed_report.html', data)

def rank_wise_students(request):
    if request.method == 'GET':
        students = Student_Rank.objects.all().order_by('student_rank')
        return render(request, 'rank_wise_student.html', {'students' : students})
        
