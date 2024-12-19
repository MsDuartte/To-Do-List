from django.contrib import admin
from django.urls import path
from tasks.views import tasks_view, new_task_view, task_detail_view, task_update_view, task_delete_view, NewTasksView, ProgressTasksView, CompletedTasksView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', tasks_view.as_view(), name='tasks_list'),
    path('tasks/new/', NewTasksView.as_view(), name='new_tasks_list'),
    path('tasks/progress/', ProgressTasksView.as_view(), name='progress_tasks_list'),
    path('tasks/completed/', CompletedTasksView.as_view(), name='completed_tasks_list'),
    path('new_task/', new_task_view.as_view(), name='new_task'),
    path('task/<int:pk>/', task_detail_view.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', task_update_view.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view.as_view(), name='task_delete'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
