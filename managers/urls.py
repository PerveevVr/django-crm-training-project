from django.urls import path

from .views import (UserEditView, 
	PasswordsChangeView, ShowProfilePageView, 
	EditProfilePageView, CreateProfilePageView,
	ManagerInterplayListView,
)


urlpatterns = [
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	path('password/', PasswordsChangeView.as_view(), name='password_change'),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
	path('interplay/', ManagerInterplayListView.as_view(), name='manager_interplay_list'),
]