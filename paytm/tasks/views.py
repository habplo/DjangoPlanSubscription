from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DeleteView
from plans.models import UserPlan
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import tasks, custtask
from .serializers import TaskSerializer
from .forms import TasksForm
from .decorators import subscription_plan_permission


@api_view(['GET'])
def getAllTask(request):
    if request.method == 'GET':
        tasks_dt = tasks.objects.filter(is_active=1)
        serializer = TaskSerializer(tasks_dt, many=True)
        return Response(serializer.data)


@subscription_plan_permission
def tasksAdd(request):
    if request.POST:
        form = TasksForm(request.POST)
    else:
        form = TasksForm()
    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        userPlan = UserPlan.objects.get(user_id=request.user.id)
        custtask.objects.create(User=request.user, tasks=task, Plan=userPlan)
        return HttpResponseRedirect(reverse('tasks_list'))
    return render(request, 'tasks/tasks_form.html', {'form': form})


class tasksListView(ListView):
    model = tasks

    def get_queryset(self):
        return super(tasksListView, self).get_queryset().all()


class TasksDeleteView(DeleteView):
    model = tasks

    def get_queryset(self):
        return super(TasksDeleteView, self).get_queryset().filter()

    def get_success_url(self):
        return reverse('tasks_list')

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        notes_dt = tasks.objects.filter(id=pk)
        notes_dt.delete()
        return HttpResponseRedirect(reverse('tasks_list', kwargs={'pk': pk}))
