from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=100, primary_key=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_id


class Subscription(models.Model):
    plans = (
        ('FREE', 'Free Plan'),
        ('MONTHLY_BASIC', 'Monthly Basic ($15/Mo)'),
        ('MONTHLY_PRO', 'Monthly Pro ($30/Mo)'),
        ('ANNUAL_PRO', 'Annual Pro ($300/Yr)'),
    )

    sub_id = models.CharField(max_length=100, primary_key=True)
    customer_id = models.ForeignKey('Customer', db_column='customer_id', on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=15, choices=plans, default='FREE')
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    initiated_on = models.DateTimeField(null=True, blank=True)
    terminated_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_id
