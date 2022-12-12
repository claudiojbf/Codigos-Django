from django.urls import path

from . import views

urlpatterns = [
    path('helloworld', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new_task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('delete/<int:id>', views.deleteTask, name='delite-task'),
    path('yourname/<str:name>', views.yourName, name = 'your-name')
]