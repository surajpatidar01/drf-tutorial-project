from django.urls import path
from . import views



urlpatterns = [
    path('students/',views.studentView),
    path('student/<int:pk>/',views.StudentDetailVew),

    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>',views.EmployeeDetail.as_view()),

]
