from django.db import models
from django.db.models.query import QuerySet
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Student_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class my_user(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

@receiver(post_save, sender=my_user)
def my_user_signal(sender, instance, **kwargs):
    print(f"My user object created.")
    print()
    print(sender, instance, kwargs)

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department']

class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self)  ->  str:
        return self.student_id

class Student(models.Model):
    student_id = models.OneToOneField(StudentId, related_name = 'studentID' , on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50, default=None)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=None)
    student_address = models.TextField(default=None)
    is_deleted = models.BooleanField(default=False, null=True)
    

    objects = Student_manager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'



class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name


class SubjectMarks(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_marks')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_marks')
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject_name} {self.marks}'
    

    class Meta:
        # For example if we have a student x and his marks in computer is a. Then there should not be another
        # record for x and subject computer. 'Student' 'Subject' combo must be remain unique.
        unique_together = ['subject', 'student']

class Student_Rank(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_rank')
    student_rank = models.IntegerField()
    date_of_generating_report = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank', 'date_of_generating_report']
    
