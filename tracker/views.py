from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Project, Ticket, Comment
from .forms import UserRegistrationForm, ProjectForm, TicketForm, TicketUpdateForm, CommentForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def dashboard(request):
    total_bugs = Ticket.objects.count()
    open_bugs = Ticket.objects.filter(status='open').count()
    resolved_bugs = Ticket.objects.filter(status='resolved').count()
    projects = Project.objects.annotate(ticket_count=Count('tickets'))

    context = {
        'total_bugs': total_bugs,
        'open_bugs': open_bugs,
        'resolved_bugs': resolved_bugs,
        'projects': projects,
    }
    return render(request, 'tracker/dashboard.html', context)


# Project Views
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'tracker/project_list.html'
    context_object_name = 'projects'

class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'tracker/project_form.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.request.user.role == 'admin'


# Ticket Views
class TicketListView(ListView):
    model = Ticket
    template_name = 'tracker/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        queryset = Ticket.objects.all()
        project_id = self.request.GET.get('project')

        if project_id:
            queryset = queryset.filter(project_id=project_id)

        return queryset

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tracker/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'tracker/ticket_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = self.object
            comment.user = request.user
            comment.save()
            return redirect('ticket_detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    template_name = 'tracker/ticket_form.html'
    
    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        # Allow if admin, or if developer and assigned
        ticket = self.get_object()
        if self.request.user.role == 'admin':
            return True
        if self.request.user.role == 'developer' and ticket.assigned_developer == self.request.user:
            return True
        return False
