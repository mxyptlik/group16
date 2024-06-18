from django.urls import path
from . import views


urlpatterns = [
    path("",views.home, name = "home"),
    path('employee/', views.employee, name = "employee"),
    path('dependent/', views.dependent, name = "dependent"),
    path('department/', views.department, name='department'),
    path('project/', views.project, name='project'),
    path('works_on/', views.works_on, name='works_on'),  
    path('forms/', views.forms, name='forms'), 
]