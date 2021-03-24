from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import EditProfileForm, PasswordChangingForm, ProfilePageForm
from main.models import Manager, Interplay


class ManagerInterplayListView(generic.ListView):
    """
    List of interactions added by the active manager.
    """
    model = Interplay
    template_name = 'list_interplay_manager.html'
    paginate_by = 4

    def setup(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(manager=self.request.user.id)
        return qs


class CreateProfilePageView(generic.CreateView):
    """
    Creating a user profile.
    """
    model = Manager
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    """
    Editing a user profile.
    """
    model = Manager
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('client_list')


class ShowProfilePageView(generic.DetailView):
    """
    View user profile.
    """
    model = Manager
    template_name = 'registration/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Manager, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class UserEditView(generic.UpdateView):
    """
    Editing user data.
    """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('client_list')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    """
    Change user password.
    """
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('client_list')
