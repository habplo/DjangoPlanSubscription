from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import tasksListView, tasksAdd, TasksDeleteView


urlpatterns = [
    url(r'^api/v1/getAllTask$', views.getAllTask, name="getAllTask"),
    path('list/', login_required(tasksListView.as_view()), name="tasks_list"),
    path('add/', login_required(views.tasksAdd), name="tasks_add"),
    path('del/<int:pk>/', login_required(TasksDeleteView.as_view()), name="tasks_del"),
]
