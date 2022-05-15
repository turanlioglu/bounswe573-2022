from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()


    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['course_name']

class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name="enrollments",on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="user_courses", on_delete=models.CASCADE)

    def __str__(self):
        self.student.username

    class Meta:
        unique_together = ('course', 'student')