from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('snippet/', views.SnippetList.as_view()),
    path('snippet/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)