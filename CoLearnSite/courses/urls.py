from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from courses import views
from courses.views import searchCourse

app_name = "courses"

urlpatterns = [
    path('new/', views.CreateCourse.as_view(), name="create"),
    path('detail/<int:pk>/', views.CourseDetail.as_view(), name='detail'),
    path('all/', views.ListCourse.as_view(), name="list"),
    path('enroll/<int:pk>/', views.EnrollCourse.as_view(), name='enroll'),
    path('unenroll/<int:pk>/', views.UnenrollCourse.as_view(), name='unenroll'),
    path('search/', searchCourse, name = "search_course"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)