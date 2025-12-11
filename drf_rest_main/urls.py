
from django.contrib import admin
from django.urls import path
from django.urls import include



# from api.views import

urlpatterns = [

    path('admin/', admin.site.urls),

    # web application endpoint
    path('students/',include('students.urls')),

    #api endpoints
    path('api/v1/',include('api.urls')),

]
