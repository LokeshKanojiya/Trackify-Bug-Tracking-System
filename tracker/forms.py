from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project, Ticket, Comment

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'screenshot', 'project']

class TicketUpdateForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'assigned_developer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Show only users with role = developer in the dropdown
        self.fields['assigned_developer'].queryset = User.objects.filter(role='developer')

        # Placeholder text instead of ---------
        self.fields['assigned_developer'].empty_label = "Select developer"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
