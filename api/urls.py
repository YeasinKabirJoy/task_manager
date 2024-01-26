from django.urls import path
from .views import all_tasks,create_task,update_task,delete_task
urlpatterns = [
    path('api/create_task', create_task,name="api-create-task"),
    path('api/all_task', all_tasks,name="api-all-task"),
    path('api/update_task/<uuid:id>', update_task,name="api-update-task"),
    path('api/delete_task/<uuid:id>', delete_task,name="api-delete-task"),

]
