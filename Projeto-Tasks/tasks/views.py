from tasks.models import Task
from tasks.forms import TaskModelForm, TaskUpdateForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q


@method_decorator(login_required(login_url='login'), name="dispatch")
class tasks_view(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Filtra as tarefas pelo usuário atualmente logado
        queryset = Task.objects.filter(user=self.request.user).order_by('-created')
      
        # Obter o parâmetro de pesquisa da solicitação
        search_query = self.request.GET.get('search', None)
        if search_query:
            # Adiciona filtro adicional para pesquisa
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(describe__icontains=search_query))
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')

        # Filtrar e limitar tarefas em cada categoria
        tasks_queryset = self.get_queryset()
        context['search'] = search_query
        context['tasks_new'] = tasks_queryset.filter(status='NewTask')[:5]  # Limite de 5
        context['tasks_in_progress'] = tasks_queryset.filter(status='InProgress')[:5]  # Limite de 5
        context['tasks_completed'] = tasks_queryset.filter(status='Completed')[:5]  # Limite de 5

        # Contar todas as tarefas (sem limite)
        context['tasks_new_count'] = tasks_queryset.filter(status='NewTask').count()
        context['tasks_in_progress_count'] = tasks_queryset.filter(status='InProgress').count()
        context['tasks_completed_count'] = tasks_queryset.filter(status='Completed').count()

        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewTasksView(ListView):
    model = Task
    template_name = 'tasks_new_list.html'  # Novo template para a lista de novas tarefas
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, status='NewTask').order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contador de tarefas
        context['tasks_new_count'] = Task.objects.filter(user=self.request.user, status='NewTask').count()
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProgressTasksView(ListView):
    model = Task
    template_name = 'tasks_progress_list.html'  # Novo template para a lista de novas tarefas
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, status='InProgress').order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contador de tarefas
        context['tasks_in_progress_count'] = Task.objects.filter(user=self.request.user, status='InProgress').count()
        return context
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CompletedTasksView(ListView):
    model = Task
    template_name = 'tasks_completed_list.html'  # Novo template para a lista de novas tarefas
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, status='Completed').order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contador de tarefas
        context['tasks_completed_count'] = Task.objects.filter(user=self.request.user, status='Completed').count()
        return context


@method_decorator(login_required(login_url='login'), name="dispatch")
class new_task_view(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'new_task.html'
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class task_detail_view(DetailView):
    model = Task
    template_name = 'task_detail.html'


@method_decorator(login_required(login_url='login'), name="dispatch")
class task_update_view(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update.html'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name="dispatch")
class task_delete_view(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = '/tasks/'