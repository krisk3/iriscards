from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('create/', views.ContactCreateView.as_view(), name="create"),
    path('profile/<str:email>', views.ProfileDetailView.as_view(), name="profile"),
    path('edit/<str:pk>', views.ProfileEditView.as_view(), name="edit"),

]