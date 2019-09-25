from django.contrib import admin
from django.contrib.auth.models import User
from .models import tasks, custtask


# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_delete', 'created_at')


class CusttaskAdmin(admin.ModelAdmin):
    list_display = ('User', 'tasks', 'Plan', 'is_active', 'is_delete', 'created_at')


admin.site.register(tasks)
admin.site.register(custtask, CusttaskAdmin)
