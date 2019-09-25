from django.db import models
from django.contrib.auth.models import User
from plans.models import UserPlan, PlanPricing, Plan, Order, BillingInfo


class notes(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    notes_desc = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (("add_only_10_notes", "To provide 10 notes facility"),
                       ("add_only_20_notes", "To provide 20 notes facility"))

    def __str__(self):
        return self.title


class custnote(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.ForeignKey(notes, on_delete=models.CASCADE, blank=True, null=True)
    Plan = models.ForeignKey(UserPlan, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)