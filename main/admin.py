"""
Registration and configuration of models 
on the administrative part of the site.
"""

from django.contrib import admin

from .models import Client, Phone, Email, Project, Interplay, Manager


admin.site.register(Manager)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('name', 'contact', 'address', 'date_creat', 'date_updat')
	search_fields = ('name',)
	ordering = ('name', 'date_creat')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
	list_display = ('client', 'category', 'number')


@admin.register(Email)
class PhoneAdmin(admin.ModelAdmin):
	list_display = ('client', 'email')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'client', 'price', 'start_date', 'end_date')
	# search_fields = ('name',)
	list_display_links = ('name',)
	list_editable = ('price',)
	ordering = ('name', 'start_date', 'end_date')
	fields = ('name', 'client', 'price', 'descript', ('start_date', 'end_date'))


@admin.register(Interplay)
class InterplayAdmin(admin.ModelAdmin):
	list_display = ('project', 'manager', 'type_comm', 'channel', 'date_comm','rating')
	list_display_links = ('project',)
	fields = (('project', 'manager'), ('type_comm', 'channel', 'rating'), 'tags','descript')
