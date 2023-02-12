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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.ContactCreateView.as_view(), name="create"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/<str:pk>', views.ProfileDetailView.as_view(), name="profile"),
    path('edit/<str:pk>', views.ProfileEditView.as_view(), name="edit"),
    path('editprofilepic/<str:pk>', views.ProfilePicEditView.as_view(), name="edit_profile_pic"),
    path('editbrochure/<str:pk>', views.BrouchureEditView.as_view(), name="edit_brochure"),
    path('editprofilenbrochure/<str:pk>', views.ProfilePicAndBrochureEditView.as_view(), name="edit_profile_and_brochure"),
    path('contact/<str:pk>', views.create_contact, name="create_contact"),
    path('download-brochure/<str:pk>', views.BrochureDownloadView.as_view(), name="create_contact"),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = "Iris Cards"
admin.site.site_title = "Iris Cards"
admin.site.index_title = "Welcome to Iris Cards Admin Portal"