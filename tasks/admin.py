from django.contrib import admin
from .models import Task,TaskImage

class TaskAdmin(admin.ModelAdmin):
    fields = ('user','title', 'description', 'due_date', 'priority', 'is_complete')
    ordering = ('-priority',)

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskImage)