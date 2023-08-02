from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_simple_mail():
    send_mail(
        'Test mail from Student report card.',
        'This is a test mail.',
        settings.EMAIL_HOST_USER, 
        ['2020cs666@student.uet.edu.pk'],
        fail_silently=False        
    )

def send_mail_with_Attachment():
    mail = EmailMessage(
        subject = 'Attachment Mail', 
        body = 'This is body of mail with attachment.',
        from_email= settings.EMAIL_HOST_USER,
        to=['2020cs666@student.uet.edu.pk']
    )
    file_path = r"D:\Hassan\this.txt"
    mail.attach_file(file_path)
    mail.send()