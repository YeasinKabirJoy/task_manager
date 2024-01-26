from django.shortcuts import render,redirect
from django.views import View
from .models import Task,TaskImage
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required, name='dispatch')
class CreateTask(View):
    def post(self,request):
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            images = request.FILES.getlist('image')
            task = task.save()
            for image in images:
                task_image = TaskImage.objects.create(task=task,image=image)
                task_image.save()
            return redirect('all-task')

    def get(self,request):
        task_form = TaskForm()
        context = {
            'task_form': task_form,
        }

        return render(request, 'task_manager/crate_task.html', context)

@method_decorator(login_required, name='dispatch')
class UpdateTask(View):
    def post(self,request,id):
        task = get_object_or_404(Task,id=id)
        task_form = TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            images = request.FILES.getlist('image')
            task = task.save()
            for image in images:
                task_image = TaskImage.objects.create(task=task,image=image)
                task_image.save()
            return redirect('update-task',task.id)

    def get(self,request,id):
        task = get_object_or_404(Task, id=id)
        images = task.taskimage_set.all()
        task_form = TaskForm(instance=task)
        context = {
            'task_form': task_form,
            'images':images,
        }

        return render(request, 'task_manager/crate_task.html', context)


@method_decorator(login_required, name='dispatch')
class AllTasks(View):
    def get(self, request):
        search_text = ""

        if request.GET.get('search-text'):
            search_text = request.GET.get('search-text')
        tasks = Task.objects.all().filter(title__contains=search_text)
        context = {
            'tasks': tasks
        }
        return render(request, 'task_manager/all_tasks.html', context)


@method_decorator(login_required, name='dispatch')
class SingleTask(View):
    def get(self,request,id):
        task = get_object_or_404(Task,id=id)
        images = task.taskimage_set.all()
        context = {
            'task':task,
            'images':images
        }
        return render(request,'task_manager/single_task.html',context)


@method_decorator(login_required, name='dispatch')
class DeleteTask(View):
    def post(self,request,id):
        task = get_object_or_404(Task,id=id)
        task.delete()
        return redirect('all-task')

    def get(self,request,id):
        task = get_object_or_404(Task,id=id)
        context = {
            'task':task,
        }
        return render(request,'task_manager/delete-task-confirmation.html',context)