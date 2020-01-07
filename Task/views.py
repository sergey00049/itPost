from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'Task/main.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = []
        for task in Task.objects.all():
            if task.author.username == self.request.user.username:
                tasks.append(task)
        return tasks
    


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'text']
    template_name_suffix = '_update_form'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('home')

