from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import mimetypes
import os

# Create your views here.

def index(request):
    return render(request, 'adminPanel/index.html')


def success(request):
    return render(request, 'adminPanel/success.html')    

def download_file(request, file_path):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = file_path 
    # Define the full file path
    filepath = BASE_DIR + '/contact/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
    


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('success'))
                #return render(request, 'adminPanel/upload.html', {})
                #it was an httpresponseredirect instead of render

            else:
                return HttpResponse("Account not Active")

        else:
            print("Someone tried to login and failed to login.")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid Login Details")

    else:
        return render(request, 'adminPanel/userLogin.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in")






