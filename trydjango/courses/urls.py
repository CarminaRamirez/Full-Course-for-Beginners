from django.urls import path
from .views import (
    CourseView,
    my_fbv,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)

app_name = 'courses'
urlpatterns = [
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('create/', CourseCreateView.as_view(), name = 'courses-create'),
    path('', CourseListView.as_view(), name = 'courses-list'),
    path('<int:id>/', CourseView.as_view(), name = 'courses-detail')
]