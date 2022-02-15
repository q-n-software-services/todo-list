from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo),
    path('todo/add_todo/', views.add_todo),
    path('todo/delete_todo/<int:todo_id>/', views.del_todo),
]
