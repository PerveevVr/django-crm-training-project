from django import forms
from django.forms.models import inlineformset_factory

from .models import Client, Phone, Email, Project, Interplay


# Working with the Client base

class ClientAddForm(forms.ModelForm):
    """Form class for creating a new client."""
    
    class Meta:
        model = Client
        fields = ('name', 'contact', 'address', 'descript')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 
                'placeholder': "название"}),
            'contact': forms.TextInput(attrs={'class': "form-control", 
                'placeholder': "Ф.И.О. (должность)"}),
            'address': forms.TextInput(attrs={'class': "form-control",
                'placeholder': "Юридический адрес клиента"}),
            'descript': forms.Textarea(attrs={'class': "form-control"}),
        }


class ClientEditForm(forms.ModelForm):
    """Form class for editing client data."""
    
    class Meta:
        model = Client
        fields = ('name', 'contact', 'address', 'descript')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'contact': forms.TextInput(attrs={'class': "form-control"}),
            'address': forms.TextInput(attrs={'class': "form-control"}),
            'descript': forms.Textarea(attrs={'class': "form-control"}),
        }

# Embeddable form sets for adding email.
EmailFormSetAdd = inlineformset_factory(
    Client, 
    Email, 
    fields=('email',),
    widgets = {'email': forms.TextInput(attrs={'class': "form-control"})},
)

#Embeddable formsets for adding phones.
PhoneFormSetAdd = inlineformset_factory(
    Client,
    Phone, 
    fields=('number','category'),
    widgets = {
        'number': forms.TextInput(attrs={'class': "form-control"}),
        'category': forms.Select(attrs={'class': "form-control"}),
    },
)

# Embeddable formsets for editing email.
EmailFormSetEdit = inlineformset_factory(
    Client, 
    Email, 
    fields=('email',),
    widgets = {'email': forms.TextInput(attrs={'class': "form-control"})},
    extra=1,
    can_delete=True,
)

# Embeddable form sets for editing phones.
PhoneFormSetEdit = inlineformset_factory(
    Client,
    Phone, 
    fields=('number','category'),
    widgets = {
        'number': forms.TextInput(attrs={'class': "form-control"}),
        'category': forms.Select(attrs={'class': "form-control"}),
    },
    extra=1,
    can_delete=True,
)


# Working with the Project base

class ProjectAddForm(forms.ModelForm):
    """Form class for creating a new project."""

    class Meta:
        model = Project
        fields = ('name', 'client', 'price', 'descript', 'start_date', 'end_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 
                'placeholder': "название"}),
            'client': forms.Select(attrs={'class': "form-control"}),
            'price': forms.NumberInput(attrs={'class': "form-control", 'id':'number_field',
                'style':'width:20ch','placeholder': "0.00"}),
            'descript': forms.Textarea(attrs={'class': "form-control"}),
            'start_date': forms.DateTimeInput(format='%d.%m.%Y %H:%M',
                attrs={'class': "form-control"}),
            'end_date': forms.DateTimeInput(format='%d.%m.%Y %H:%M',
                attrs={'class': "form-control"}),
        }

    def clean_end_date(self):
        """Checking the project completion date."""
        end_data = self.cleaned_data['end_date']
        if end_data < self.cleaned_data['start_date']:
            raise forms.ValidationError('Неверная дата! Дата завершения проекта не может быть раньше даты начала.')
        return end_data


class ProjectEditForm(forms.ModelForm):
    """Form class for editing project data."""

    class Meta:
        model = Project
        fields = ('name', 'price', 'descript', 'start_date', 'end_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'price': forms.NumberInput(attrs={'class': "form-control",
                'id':'number_field', 'style':'width:20ch'}),
            'descript': forms.Textarea(attrs={'class': "form-control"}),
            'start_date': forms.DateTimeInput(format='%d.%m.%Y %H:%M',
                attrs={'class': "form-control"}),
            'end_date': forms.DateTimeInput(format='%d.%m.%Y %H:%M',
                attrs={'class': "form-control"}),
        }

    def clean_end_date(self):
        """Checking the project completion date"""
        end_data = self.cleaned_data['end_date']
        if end_data < self.cleaned_data['start_date']:
            raise forms.ValidationError('Неверная дата! Дата завершения проекта не может быть раньше даты начала.')
        return end_data


# Working with the Interplay base

class InterplayAddForm(forms.ModelForm):
    """The form class for creating the interaction."""

    class Meta:
        model = Interplay
        fields = ('project', 'manager', 'type_comm', 'channel', 'rating', 'descript', 'tags')

        widgets = {
            'project': forms.Select(attrs={'class': "form-control"}),
            'manager': forms.TextInput(attrs={'class': "form-control", 
                'value':'', 'id':'elder', 'type':'hidden'}),
            'type_comm': forms.Select(attrs={'class': "form-control"}),
            'channel': forms.Select(attrs={'class': "form-control"}),
            'rating': forms.NullBooleanSelect(attrs={'class': "form-control"}),
            'descript': forms.Textarea(attrs={'class': "form-control"}),
            'tags': forms.TextInput(attrs={'class': "form-control"}),
        }


class InterplayEditForm(forms.ModelForm):
    """Form class for editing interaction data."""
        
    class Meta:
        model = Interplay
        fields = ('type_comm', 'channel', 'rating', 'descript', 'tags')

        widgets = {
            'type_comm': forms.Select(attrs={'class': "form-control"}),
            'channel': forms.Select(attrs={'class': "form-control"}),
            'rating': forms.NullBooleanSelect(attrs={'class': "form-control"}),
            'descript': forms.Textarea(attrs={'class': "form-control"}),
            # 'tags': forms.TextInput(attrs={'class': "form-control"}),
        }
