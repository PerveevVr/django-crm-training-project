from django.urls import path

from .views import (
	ClientListView, ClientDetailView, ClientAddView, 
	ClientUpdateView, ClientDeleteView,
	ProjectListView, ProjectDetailView, ProjectUpdateView,
	ProjectAddView, ProjectDeleteView,
	ClientProjectView,
    InterplayListView, InterplayAddView, InterplayDetailView,
    InterplayUpdateView, InterplayDeleteView,
    ClientInterplayView, ProjectInterplayView,
)

urlpatterns = [
    
    path('', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientAddView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/remove/', ClientDeleteView.as_view(), name='client_delete'),
    path('client/<int:pk>/project/', ClientProjectView.as_view(), name='client_project'),
    path('client/<int:pk>/interplay/', ClientInterplayView.as_view(), name='client_interplay'),
    
    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/add/', ProjectAddView.as_view(), name='project_create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/remove/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/interplay/', ProjectInterplayView.as_view(), name='project_interplay'),

    path('interplay/', InterplayListView.as_view(), name='interplay_list'),
    path('interplay/add/', InterplayAddView.as_view(), name='interplay_create'),
    path('interplay/<int:pk>/', InterplayDetailView.as_view(), name='interplay_detail'),
    path('interplay/<int:pk>/edit/', InterplayUpdateView.as_view(), name='interplay_update'),
    path('interplay/<int:pk>/remove/', InterplayDeleteView.as_view(), name='interplay_delete'),

    path('<sort>/', ClientListView.as_view(), name='client_list'),
]
