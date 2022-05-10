from django.urls import path
from courses import views

app_name = "courses"

urlpatterns = [
    path('new/', views.CreateCourse.as_view(), name="create"),
    path('detail/<int:pk>/', views.CourseDetail.as_view(), name='detail'),
    path('all/', views.ListCourse.as_view(), name="list"),
    path('enroll/<int:pk>/', views.EnrollCourse.as_view(), name='enroll'),
    path('unenroll/<int:pk>/', views.UnenrollCourse.as_view(), name='unenroll'),
]