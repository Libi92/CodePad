import json
import os
import datetime
from django.contrib.sessions.models import Session
from django.core.files import File
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from codepadapp.forms import ChangePasswordForm
from codepadapp.models import Lab, Login, UserPrograms, ExamMarks
from codepadapp.utils.run import runProcess




def index(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            id = request.session['id']
            login = Login.objects.get(pk=id)
            if login.password == form.cleaned_data['currentpassword']:
                login.password = form.cleaned_data['newpassword']
                login.save()
                request.session['alert'] = "Password Changed"
            else:
                request.session['alert'] = "Password mismatch"
    form = ChangePasswordForm()
    return render(request, 'Students/index.html', {'form': form})


def lab(request):
    data = Lab.objects.all()
    return render(request, 'Students/lab.html', {'labs': data})

def runprogram(request, lab):
    lab_object = Lab.objects.get(pk=lab)
    if lab_object.language == 'C':
        filepath = "codepadapp/code/stub/c"
    elif lab_object.language == 'Java':
        filepath = "codepadapp/code/stub/java"
    else:
        filepath = "codepadapp/code/stub/cpp"
    file = open(filepath)

    programs = UserPrograms.objects.filter(lab=lab_object)
    return render(request, 'Students/runprogram.html', {'lab': lab_object, 'stub': file.read(), 'programs': programs})


def execprogram(request):
    name = request.GET['name']
    code = request.GET['code']
    language = request.GET['language']
    command = request.GET['command']
    print("./a.out " + command)
    if language == 'Java':
        filepath = "codepadapp/code/" + name + ".java"
        file = open(filepath, 'w+')
        file.write(code)
        file.close()
        abs_path = os.path.abspath(file.name)
        print(abs_path)
        error = runProcess(["javac", abs_path])
        if not error:
            print("Compiled")

            output = runProcess(["java", "-cp", "codepadapp/code", name, command])
            for line in output:
                result = line + "\r\n"
        else:
            for line in error:
                result = line + "\r\n"

        os.remove(abs_path)
    elif language == 'C':
        filepath = "codepadapp/code/" + name + ".c"
        file = open(filepath, 'w+')
        file.write(code)
        file.close()
        abs_path = os.path.abspath(file.name)
        print(abs_path)
        error = runProcess(["gcc", abs_path])
        if not error:
            print("Compiled")

            output = runProcess(["./a.out", command])
            for line in output:
                result = line + "\r\n"
        else:
            for line in error:
                result = line + "\r\n"

        os.remove(abs_path)
    else:
        filepath = "codepadapp/code/" + name + ".cpp"
        file = open(filepath, 'w+')
        file.write(code)
        file.close()
        abs_path = os.path.abspath(file.name)
        print(abs_path)
        error = runProcess(["g++", abs_path])
        if not error:
            print("Compiled")

            output = runProcess(["./a.out"])
            for line in output:
                result = line + "\r\n"
        else:
            for line in error:
                result = line + "\r\n"

        os.remove(abs_path)

    return HttpResponse(result)


def downloadprogram(request, name, program):

    print(name)
    print(program)
    file_name = "Hello.java"
    path_to_file = "codepadapp/code/Hello.java"
    f = open(path_to_file, 'r')
    myfile = File(f)
    response = HttpResponse(myfile, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response


def save_program(request):
    name = request.GET['name']
    code = request.GET['code']
    language = request.GET['language']
    lab = request.GET['lab']
    id = request.session['id']
    directory = os.path.join("codepadapp", "code", str(id), language)

    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join("codepadapp", "code", str(id), language, name + "." + language.lower())
    file = open(filepath, 'w+')
    file.write(code)
    file.close()

    login = Login.objects.get(pk=id)
    lab = Lab.objects.get(pk=lab)

    program = UserPrograms()
    program.loginid = login
    program.programname = name
    program.lab = lab
    program.language = language
    program.path = filepath
    program.date = datetime.datetime.now()
    program.save()

    return HttpResponse("program saved")


def get_saved_programs(request):
    id = request.GET['id']
    program = UserPrograms.objects.get(pk=id)
    file = open(program.path, 'r')
    text = file.read()
    data = [program.programname, text]

    return HttpResponse(json.dumps(data))


def exam(request):
    marks = ExamMarks.objects.filter(login=Login.objects.get(pk=request.session['id']))
    return render(request, 'Students/exam.html', {'marks': marks})


def contact(request):
    return render(request, 'Students/contact.html')


def logout(request):
    Session.objects.all().delete()
    return HttpResponseRedirect('/')