from django.db import models
from django.db.models import ForeignKey
from django.conf import settings


class Course(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.TextField()
    course_category = models.CharField(max_length=100)
    course_instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_title


class Session(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'برگزار می‌شود'),
        ('cancelled', 'لغو شده'),
        ('completed', 'برگزار شده'),
    )
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.course.course_title} - {self.start_time}"


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    session = models.ForeignKey('Session', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'session']

    def __str__(self):
        return f"{self.student.username} - {self.session.course.course_title}"
