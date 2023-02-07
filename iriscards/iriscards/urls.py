"""iriscards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.ContactCreateView.as_view(), name="create"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/<str:pk>', views.ProfileDetailView.as_view(), name="profile"),
    path('edit/<str:pk>', views.ProfileEditView.as_view(), name="edit"),
    path('contact/<str:pk>', views.create_contact, name="create_contact"),
]


admin.site.site_header = "Iris Cards"
admin.site.site_title = "Iris Cards"
admin.site.index_title = "Welcome to Iris Cards Admin Portal"