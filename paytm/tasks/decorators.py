from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from plans.models import UserPlan
from .models import custtask


def subscription_plan_permission(function):
    def plan(request, *args, **kwargs):
        userPlan = UserPlan.objects.get(user_id=request.user.id)
        tasks_dt = custtask.objects.filter(User=request.user).count()
        if str(userPlan.plan) == "Basic" and tasks_dt >= 5:
            messages.error(request, mark_safe('Please upgrade your plan to create more task! <a href="/plan/upgrade">('
                                              'upgrade)</a>'), extra_tags='safe')
            return redirect('tasks_list')
            raise PermissionDenied
        elif str(userPlan.plan) == "Standard" and tasks_dt >= 10:
            messages.error(request, mark_safe('Please upgrade your plan to create more task! <a href="/plan/upgrade">('
                                              'upgrade)</a>'), extra_tags='safe')
            return redirect('tasks_list')
            raise PermissionDenied
        else:
            return function(request, *args, **kwargs)

    plan.__doc__ = function.__doc__
    plan.__name__ = function.__name__
    return plan