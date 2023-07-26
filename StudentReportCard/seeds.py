from faker import Faker
import random
from .models import *
fake = Faker()

# def seed_dept():
#     Department.objects.create(department_name = "Computer Sciences")
#     Department.objects.create(department_name = "Mechanical Engineering")
#     Department.objects.create(department_name = "Electrical Engineering")
#     Department.objects.create(department_name = "Civil Engineering")

def seed_db():
    try:
        for i in range(10):
            department_obj = Department.objects.all()
            random_index = random.randint(0, len(department_obj)-1)
            department = department_obj[random_index]
            my_student_id = f"STU-{random.randint(100, 999)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 24)
            student_address = fake.address()

            student_id_obj = StudentId.objects.create(student_id = my_student_id)

            student_obj = Student.objects.create(
                student_name = student_name,
                student_id = student_id_obj, 
                department = department,
                student_email = student_email,
                student_age = student_age, 
                student_address = student_address
            )
    except Exception as e :
        print(e)