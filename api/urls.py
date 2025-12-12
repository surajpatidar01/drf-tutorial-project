from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentView),
    path('student/<int:pk>/', views.StudentDetailVew),

    path('', include(router.urls))
]
