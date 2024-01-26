from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from tasks.models import Task

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_task(request,id):
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(data={'message':"Not Found"},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_task(request,id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return Response(data={'message':"Delete"}, status=status.HTTP_200_OK)
    except:
        return Response(data={'message':"Not Found"},status=status.HTTP_404_NOT_FOUND)