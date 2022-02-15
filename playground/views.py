from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . import models


# Create your views here.


def todo(request):
    todo_items = models.todo.objects.all().order_by("-added_date")

    return render(request, 'base.html', {
        "todo_items": todo_items
    })


@csrf_exempt
def add_todo(request):

    currentdate = timezone.now()
    content = request.POST["content"]
    created_obj = models.todo.objects.create(added_date=currentdate, text=content)
    todo_items = models.todo.objects.all().order_by("-added_date")


    return render(request, 'base.html', {
        'todo_items': todo_items
    })

@csrf_exempt
def del_todo(request, todo_id):
    print(todo_id)
    models.todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect("http://127.0.0.1:1292/playground/todo/")
