from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from taggit.models import Tag

from .models import Client, Phone, Email, Project, Interplay
from .forms import (
    ClientAddForm, ClientEditForm, 
    ProjectAddForm, ProjectEditForm,
    InterplayAddForm, InterplayEditForm,
    PhoneFormSetAdd, EmailFormSetAdd,
    PhoneFormSetEdit, EmailFormSetEdit,
)


# Working with the Client base

class ClientListView(generic.ListView):
    """
    Forms a list of all customers with the ability 
    to sort by name (direct), by name (reverse), 
    by date of creation (direct) and by date of 
    creation (reverse). Searches for clients 
    by the requested keyword.
    """
    model = Client
    template_name = 'list_client.html'
    paginate_by = 3
    
    def get_ordering(self):
        ordering = self.kwargs.get('sort', None)
        if ordering == 'name':
            order = 'name'
        elif ordering == 'namer':
            order = '-name'
        elif ordering == 'dc':
            order = 'date_creat'
        elif ordering == 'dcr':
            order = '-date_creat'
        else:
            order = ''
        return order

    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        project_word = self.request.GET.get('word')
        if project_word:
            qs = qs.filter(name__icontains=project_word)
            self.paginate_by = None
        return qs


class ClientAddView(generic.CreateView):
    """
    Forms a new client. Creation of data for a new client.
    """
    model = Client
    form_class = ClientAddForm
    template_name = 'add_client.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_form = PhoneFormSetAdd()
        email_form = EmailFormSetAdd()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  phone_form=phone_form,
                                  email_form=email_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_form = PhoneFormSetAdd(self.request.POST)
        email_form = EmailFormSetAdd(self.request.POST)
        if (form.is_valid() and phone_form.is_valid() and
            email_form.is_valid()):
            return self.form_valid(form, phone_form, email_form)
        else:
            return self.form_invalid(form, phone_form, email_form)

    def form_valid(self, form, phone_form, email_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        phone_form.instance = self.object
        phone_form.save()
        email_form.instance = self.object
        email_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, phone_form, email_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  phone_form=phone_form,
                                  email_form=email_form))


class ClientDetailView(generic.DetailView):
    """
    Forms detailed information about the client.
    """
    model = Client
    template_name = 'detail_client.html'


class ClientUpdateView(generic.UpdateView):
    """
    Forms editing of customer data.
    """
    model = Client
    template_name = 'update_client.html'
    form_class = ClientEditForm

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['phone_form'] = PhoneFormSetEdit(self.request.POST, 
                instance=self.object)
            context['email_form'] = EmailFormSetEdit(self.request.POST, 
                instance=self.object)
        else:
            context['phone_form'] = PhoneFormSetEdit(instance=self.object)
            context['email_form'] = EmailFormSetEdit(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_form = PhoneFormSetEdit(self.request.POST)
        email_form = EmailFormSetEdit(self.request.POST)
        if (form.is_valid() and phone_form.is_valid() and
            email_form.is_valid()):
            return self.form_valid(form, phone_form, email_form)
        else:
            return self.form_invalid(form, phone_form, email_form)

    def form_valid(self, form, phone_form, email_form):
        context = self.get_context_data()
        phone_form = context['phone_form']
        email_form = context['email_form']
        if phone_form.is_valid() and email_form.is_valid():
            self.object = form.save()
            phone_form.instance = self.object
            phone_form.save()
            email_form.instance = self.object
            email_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, phone_form, email_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  phone_form=phone_form,
                                  email_form=email_form))


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Forms a client deletion.
    """
    model = Client
    template_name = 'delete_client.html'
    success_url = reverse_lazy('client_list')


# Working with the Project base

class ProjectListView(generic.ListView):
    """
    Forms a list of all projects. The ability 
    to search for information by keyword.
    """
    model = Project
    template_name = 'list_project.html'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        project_word = self.request.GET.get('word')
        if project_word:
            qs = qs.filter(name__icontains=project_word)
            self.paginate_by = None
        return qs 


class ProjectAddView(generic.CreateView):
    """
    Class for creating a new project.
    """
    model = Project
    form_class = ProjectAddForm
    template_name = 'add_project.html'


class ProjectDetailView(generic.DetailView):
    """
    Forms detailed information about the project.
    """
    model = Project
    template_name = 'detail_project.html'


class ProjectUpdateView(generic.UpdateView):
    """
    Forms editing of project data.
    """
    model = Project
    template_name = 'update_project.html'
    form_class = ProjectEditForm


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Forms the deletion of the project.
    """
    model = Project
    template_name = 'delete_project.html'
    success_url = reverse_lazy('project_list')



# Working with the Interplay base

class InterplayListView(generic.ListView):
    """
    Generates a list of all interactions.
    """
    model = Interplay
    template_name = 'list_interplay.html'
    paginate_by = 4

    def get_queryset(self, *args, **kwargs): 
        qs = super(InterplayListView, self).get_queryset(*args, **kwargs) 
        
        # Filter by tags
        tags = None
        tags = self.request.GET.get('tags')
        print(tags)
        if tags:
            tags = tags.replace(',', '').split()
            print(tags)
            qs = qs.filter(tags__slug__in=tags)
            self.paginate_by = None
        
        return qs 


class InterplayAddView(generic.CreateView):
    """
    Forms a new interaction.
    """
    model = Interplay
    form_class = InterplayAddForm
    template_name = 'add_interplay.html'


class InterplayDetailView(generic.DetailView):
    """
    Forms detailed information interaction.
    """
    model = Interplay
    template_name = 'detail_interplay.html'


class InterplayUpdateView(generic.UpdateView):
    """
    Generates interaction data editing.
    """
    model = Interplay
    template_name = 'update_interplay.html'
    form_class = InterplayEditForm


class InterplayDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Forms a deletion interaction.
    """
    model = Interplay
    template_name = 'delete_interplay.html'
    success_url = reverse_lazy('interplay_list')



class ClientProjectView(generic.DetailView):
    """
    Forms a list of all projects for the client.
    """
    model = Client
    template_name = 'client_project.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClientProjectView, self).get_context_data(*args, **kwargs)
        
        project_word = self.request.GET.get('word')
        client = kwargs['object']
        project_set = Project.objects.filter(client_id=client)
        quantity_project = project_set.count()
        
        if project_word:
            project_set = project_set.filter(name__icontains=project_word)
            # project_set = project_set.filter(name__iexact=project_word)
            context['projects'] = project_set
        else:    
            context['projects'] = project_set

        context['quantity_project'] = quantity_project
        # print(context)
        return context


class ClientInterplayView(generic.DetailView):
    """
    Generates a list of all customer interactions.
    """
    model = Client
    template_name = 'client_interplay.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInterplayView, self).get_context_data(**kwargs)
        client = kwargs['object']
        interplay_set = Interplay.objects.filter(project__client_id=client)
        quantity_interplay = interplay_set.count()
        context['interplays'] = interplay_set
        context['quantity_interplay'] = quantity_interplay
        return context


class ProjectInterplayView(generic.DetailView):
    """
    Generates a list of all project interactions.
    """
    model = Project
    template_name = 'project_interplay.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectInterplayView, self).get_context_data(**kwargs)
        project = kwargs['object']
        interplay_set = Interplay.objects.filter(project_id=project)
        quantity_interplay = interplay_set.count()
        context['interplays'] = interplay_set
        context['quantity_interplay'] = quantity_interplay
        return context



# on 404 error
def error_404_view(request, exception):
    return render(request, '404.html')
