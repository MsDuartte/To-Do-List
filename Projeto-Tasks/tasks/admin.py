from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'describe','created', 'datecompleted', 'status')
    search_fields = ('id',)

admin.site.register(Task, TaskAdmin)