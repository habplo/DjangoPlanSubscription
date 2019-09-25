from django.contrib import admin
from .models import Subscription, Customer


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('sub_id', 'customer_id', 'plan_type', 'initiated_on', 'terminated_on', 'is_active')
    list_filter = ('plan_type', 'initiated_on', 'is_active')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'customer_id', 'is_active', 'is_delete', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_delete', 'created_at')


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Customer, CustomerAdmin)
