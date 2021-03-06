from django.db import models
from django.urls import reverse
from users.models import User
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()
    user = models.ForeignKey(User, related_name="course", on_delete=models.CASCADE)
    students = models.ManyToManyField(User, through='Enrollment', related_name="student_course")

    def courseImage(self):
        if self.course_image:
            return self.course_image.url
        return ''
        
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