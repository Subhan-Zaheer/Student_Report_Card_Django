from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.

class my_user_admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name', 'password')

admin.site.register(my_user, my_user_admin)

class my_department(admin.ModelAdmin):
    list_display = ('department_name',)

admin.site.register(Department, my_department)

class my_studentid(admin.ModelAdmin):
    list_display = ('student_id', )

admin.site.register(StudentId, my_studentid)

class my_student(admin.ModelAdmin):
    list_display = ('student_id', 'department', 'student_name', 'student_email', 'student_age', 'student_address')

admin.site.register(Student, my_student)

class my_subject(admin.ModelAdmin):
    list_display = ('subject_name',)

admin.site.register(Subject, my_subject)

class my_subject_marks(admin.ModelAdmin):
    list_display = ('subject', 'student', 'marks')

admin.site.register(SubjectMarks, my_subject_marks)

class my_student_ranks(admin.ModelAdmin):
    list_display = ('student', 'student_rank', 'total_marks', 'date_of_generating_report')
    ordering = ['student_rank']
    def total_marks(self, obj):
        student_marks = SubjectMarks.objects.filter(student = obj.student)
        marks = student_marks.aggregate(marks = Sum('marks'))
        return marks['marks']

admin.site.register(Student_Rank, my_student_ranks)

