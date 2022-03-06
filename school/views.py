from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    stud_dict = {}
    for student in students:
        stud_dict[student] = {
            'name': student.name,
            'group': student.group,
            'teacher': student.teacher
        }
    context = {'object_list': stud_dict}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
