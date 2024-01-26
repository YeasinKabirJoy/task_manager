from django.urls import path
from .views import AllTasks,CreateTask,SingleTask,DeleteTask,UpdateTask
urlpatterns = [
    path('', AllTasks.as_view(),name="all-task"),
    path('task/<uuid:id>/', SingleTask.as_view(),name="single-task"),
    path('create/', CreateTask.as_view(),name="create-task"),
    path('update/<uuid:id>/', UpdateTask.as_view(),name="update-task"),
    path('delete/<uuid:id>', DeleteTask.as_view(),name="delete-task"),

]
