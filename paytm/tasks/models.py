from django.db import models
from django.contrib.auth.models import User
from plans.models import UserPlan, PlanPricing, Plan, Order, BillingInfo


class tasks(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (("add_only_5_task", "To provide 5 task facility"),
                       ("add_only_10_task", "To provide 10 task facility"))

    def __str__(self):
        return self.title


class custtask(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.ForeignKey(tasks, on_delete=models.CASCADE, blank=True, null=True)
    Plan = models.ForeignKey(UserPlan, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)