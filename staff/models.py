from django.db import models

class StaffEmail(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()

    TEACHER = 'Teacher'
    STUDENT = 'Student'
    USER = 'User'
    P_TEACHER = 'Prospective Teacher'
    P_STUDENT = 'Prospective Student'
    PARENT = 'Parent'
    FOLLOWER = 'Follower'

    SENDTO_CHOICES = (
        (TEACHER, 'All Teachers'),
        (STUDENT, 'All Students'),
        (USER, 'All Users (Teachers and Students)'),
        (P_TEACHER, 'Prospective Teachers'),
        (P_STUDENT, 'Prospective Students'),
        (PARENT, 'Parent / Interested Person'),
        (FOLLOWER, 'Everyone on interest list'),
    )
    send_to = models.CharField(max_length=20, 
                               choices=SENDTO_CHOICES, 
                               null=True)
