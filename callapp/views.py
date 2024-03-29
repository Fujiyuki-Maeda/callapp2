from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView,FormView
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import redirect

from callapp.models import Task


# Create your views here.
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    
    def get_queryset(self):
        return Task.objects.order_by("title") # titleで昇順に並び替え
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ["title","completed"]#"__all__"
    success_url = reverse_lazy("tasks")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ["title","completed"]#"__all__"
    success_url = reverse_lazy("tasks")
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"

class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "callapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")
    
class RegisterCallApp(FormView):
    template_name = "callapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")
    
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class HomeTemplateView(TemplateView):
    # template_name = 'callapp/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Task.objects.all()
        total_titles = Task.objects.count()
        total_completed = Task.objects.filter(completed=True).count()
        total_completed_add = round(total_completed *5/2)
        total_sub = total_titles-total_completed
        multiplied_total = round(total_sub *20/3+ total_completed_add)
        context['multiplied'] = multiplied_total
        return context
    

    

