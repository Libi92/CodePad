from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect

from codepadapp.forms import LoginForm
from codepadapp.models import Login, Faculty, Students


def about(request):

    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')
def home(request):
    return render(request, 'index.html')
def contact(request):
    return render(request,'contact.html')

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login = Login.objects.filter(username=username, password=password)
            if len(login) > 0:
                if login[0].type == 'admin':
                    return HttpResponseRedirect('/Admin/home')
                elif login[0].type == 'student':
                    name = Students.objects.filter(loginid=login)[0].firstname
                    request.session['id'] = login[0].pk
                    request.session['name'] = name
                    return HttpResponseRedirect('/Student/home')
                elif login[0].type == 'faculty':
                    name = Faculty.objects.filter(loginid=login)[0].name
                    request.session['id'] = login[0].pk
                    request.session['name'] = name
                    return HttpResponseRedirect('/Faculty/home')

            elif username.startswith("exam"):
                request.session['regno'] = username.split("_")[1]
                return HttpResponseRedirect('/Exam/home')

            else:
                request.session['alert'] = 'Invalid Login'

    else:
        request.session['alert'] = None
        form = LoginForm()

    return render(request, 'index.html', {'form': form})
