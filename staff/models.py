from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()

    TEACHER = 'Teacher'
    STUDENT = 'Student'
    USER = 'User'
    FOLLOWER = 'Follower'
    SENDTO_CHOICES = (
        (TEACHER, 'All Teachers'),
        (STUDENT, 'All Students'),
        (USER, 'All Users (Teachers and Students)'),
        (FOLLOWER, 'Followers (Interested people)'),
    )
    send_to = models.CharField(max_length=10, 
                               choices=SENDTO_CHOICES, 
                               null=True)
