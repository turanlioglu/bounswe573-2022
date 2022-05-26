from django.urls import path
from resources import views

app_name = "resources"

urlpatterns = [
    path('create/', views.CreateResource.as_view(), name="create"),
    path('delete/<int:pk>', views.delete_view, name='delete')
] 