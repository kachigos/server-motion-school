from django.urls import path
from .views import CategoryCreateListView, ChronologyCreateListView, AccreditationCreateListView, TeacherCreateListView, \
CategoryDeleteView, ChronologyDeleteView, AccreditationDeleteView, TeacherDeleteView, AccreditationDetailView, CategoryDetailView


urlpatterns = [
    path('category/', CategoryCreateListView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view()),
    
    path('chronology/', ChronologyCreateListView.as_view()),
    path('chronology/delete/<int:pk>/', ChronologyDeleteView.as_view()),
    
    path('accreditation/', AccreditationCreateListView.as_view()),
    path('accreditation/detail/<int:pk>/', AccreditationDetailView.as_view()),
    path('accreditation/delete/<int:pk>/', AccreditationDeleteView.as_view()),
    
    path('teacher/', TeacherCreateListView.as_view()),
    path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view()),
]
