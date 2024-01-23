from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

def students_list(request):
    template = 'school/students_list.html'
    
    # Получаем список всех учеников
    students = Student.objects.all()

    # Передаем список учеников в контекст шаблона
    context = {'students': students}

    return render(request, template, context)
