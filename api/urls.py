from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentView),
    path('student/<int:pk>/', views.StudentDetailVew),

    path('', include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentView.as_view()),

    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view())
]

