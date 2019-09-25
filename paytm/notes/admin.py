from django.contrib import admin
from .models import notes, custnote


# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'notes_desc', 'is_active', 'is_delete', 'created_at')


class CustnoteAdmin(admin.ModelAdmin):
    list_display = ('User', 'notes', 'Plan', 'is_active', 'is_delete', 'created_at')


admin.site.register(notes, NotesAdmin)
admin.site.register(custnote, CustnoteAdmin)
