from django.urls import path
from assignments import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'assignments'
urlpatterns = [
    path('create/', views.CreateAssignment.as_view(), name="create"),
    path('detail/<int:pk>/', views.AssignmentDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateAssignment.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteAssignment.as_view(), name="delete"),
    path('submit/', views.SubmitAssignmentView.as_view(), name="submit"),
    path('submission/detail/<int:pk>/', views.SubmitAssignmentDetail.as_view(), name="submit_detail"),
    path('submission/delete/<int:pk>/', views.delete_view, name="submit_delete"),
    path('grade/<int:pk>/', views.grade_assignment, name='grade')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)