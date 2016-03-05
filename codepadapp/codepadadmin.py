import os
from django.conf import settings
from django.contrib.sessions.models import Session
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from codepadapp.forms import AddStudentsForm, LabForm, FacultyForm
import pyexcel as pe
import pyexcel.ext.xls
import pyexcel.ext.xlsx
from codepadapp.models import Students, Login, Lab, Faculty
from codepadapp.utils import helpers




def index(request):
    return render(request, 'CodepadAdmin/index.html')
def exam(request):
    return render(request, 'CodepadAdmin/exam.html')
def contact(request):
    return render(request,'CodepadAdmin/contact.html')

def lab(request):
    if request.method == 'POST':
        form = LabForm(request.POST)
        if form.is_valid():
            labmodel = Lab()
            labmodel.labname = form.cleaned_data['name']
            labmodel.semester = form.cleaned_data['semester']
            labmodel.language = form.cleaned_data['language']
            labmodel.faculty = form.cleaned_data['faculty']

            labmodel.save()
            request.session['alert'] = 'New lab added'
    else:
        request.session['alert'] = None
        form = LabForm()
    return render(request, 'CodepadAdmin/lab.html', {'form': form})


def list_faculty(request, lab):
    data = Faculty.objects.all()
    print(data)
    return render(request, 'Faculty/labstudents.html', {'students': data, 'lab': lab})

def faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            staffid = form.cleaned_data['staffid']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            login = Login()
            login.username = name.lower() + "_" + staffid
            login.password = helpers.generateRandomPassword()
            login.type = 'faculty'
            login.status = 1
            login.save()

            tomail = email
            subject = 'Codepad Faculty account created'
            message = 'Your codepad faculty account has been created. Please note the following credentials - Username : ' + login.username + ', Password : ' + login.password
            helpers.sendEmail(tomail, subject, message)

            faculty = Faculty()
            faculty.name = name
            faculty.staffid = staffid
            faculty.loginid = login
            faculty.designation = form.cleaned_data['designation']
            faculty.email = email
            faculty.phone = form.cleaned_data['phone']
            faculty.save()

    else:

        form = FacultyForm()
    data = Faculty.objects.all()
    return render(request, 'CodepadAdmin/faculty.html', {'form': form,'faculty': data})


def handle_uploaded_file(f):
    uploaddir = os.path.join(settings.BASE_DIR, 'codepadapp/uploads')
    with open(os.path.join(uploaddir, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return os.path.join(uploaddir, f.name)


def logout(request):
    Session.objects.all().delete()
    return HttpResponseRedirect('/')

def edit_Faculty(request, id):
    staf = Faculty.objects.get(pk=id)

    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
              staf.name= form.cleaned_data['name']
              staf.designation = form.cleaned_data['designation']
              staf.phone = form.cleaned_data['phone']
              staf.email = form.cleaned_data['email']
              staf.save()
              return HttpResponseRedirect('/Admin/Faculty')
    request.session['alert'] = None
    return render(request, 'CodepadAdmin/editfaculty.html', {'facult': staf})


def delete_Faculty(request, id):
    staff = Faculty.objects.get(pk=id)
    staff.delete()
    return HttpResponseRedirect('/Admin/Faculty')