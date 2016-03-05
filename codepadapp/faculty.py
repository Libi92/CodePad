import os
from twisted.test.test_jelly import E

from datetime import datetime
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CodePad import settings
from codepadapp.forms import AddStudentsForm, NewStudentForm, ChangePasswordForm, ExamForm, ExamMarksForm

import pyexcel as pe
import pyexcel.ext.xls
import pyexcel.ext.xlsx
from codepadapp.models import Login, Students, Lab, UserPrograms, Exam, ExamQuestions, ExamLogin, Faculty, ExamAnswers, \
    ExamMarks
from codepadapp.utils import helpers




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
    return render(request, 'Faculty/index.html', {'form': form})


def students(request):
    if request.method == 'POST':
        form = AddStudentsForm(request.POST, request.FILES)
        if form.is_valid():
            file = handle_uploaded_file(request.FILES['file'])

            records = pe.get_records(file_name=file)
            i = 0

            repeated = []
            students = map(lambda  s:int(s.admission_no), Students.objects.all())
            print(students)
            for record in records:

                admission_no = record['admissionno']

                if admission_no not in students:

                    login = Login()
                    username = record['firstname'].lower() + "_" + str(record['admissionno'])
                    password = helpers.generateRandomPassword()
                    login.username = username
                    login.password = password
                    login.type = 'student'
                    login.status = '1'
                    login.save()

                    tomail = record['email']
                    subject = 'Codepad Student account created'
                    message = 'Your codepad student account has been created. Please note the following credentials - Username : ' + username + ', Password : ' + password
                    helpers.sendEmail(tomail, subject, message)

                    student = Students()
                    student.loginid = login
                    student.admission_no = record['admissionno']
                    student.firstname = record['firstname']
                    student.lastname = record['lastname']
                    student.address = record['address']
                    student.contact = record['contact']
                    student.email = record['email']
                    student.department = record['department']
                    student.semester = record['semester']
                    student.save()
                    i += 1

                else:
                    repeated.append(admission_no)

            request.session['alert'] = str(i) + ' Student accounts created'

    else:
        # request.session['alert'] = None
        form = AddStudentsForm()

    data = Students.objects.all()
    return render(request, 'Faculty/students.html', {'form': form, 'students': data})




def new_student(request):
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['firstname']
            admissionno = form.cleaned_data['admission_no']

            admissionno = int(admissionno)
            students = map(lambda  s:int(s.admission_no), Students.objects.all())

            print(students)
            if admissionno not in students:
                email = form.cleaned_data['email']

                login = Login()
                login.username = name.lower() + "_" + str(admissionno)
                login.password = helpers.generateRandomPassword()
                login.type = 'student'
                login.status = 1
                login.save()

                tomail = email
                subject = 'Codepad Student account created'
                message = 'Your codepad student account has been created. Please note the following credentials - Username : ' + login.username + ', Password : ' + login.password
                helpers.sendEmail(tomail, subject, message)

                student = Students()
                student.loginid = login
                student.admission_no = admissionno
                student.firstname = name
                student.lastname = form.cleaned_data['lastname']
                student.address = form.cleaned_data['address']
                student.contact = form.cleaned_data['contact']
                student.email = email
                student.department = form.cleaned_data['department']
                student.semester = form.cleaned_data['semester']
                student.save()

                request.session['alert'] = 'New student added'
            else:
                request.session['alert'] = 'Admission No already exists'


        return HttpResponseRedirect('/Faculty/students')

    else:
        form = NewStudentForm()
        return render(request, 'Faculty/newstudent.html', {'form': form})


def edit_student(request, id):
    student = Students.objects.get(pk=id)

    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            student.admission_no = form.cleaned_data['admission_no']
            student.firstname = form.cleaned_data['firstname']
            student.lastname = form.cleaned_data['lastname']
            student.address = form.cleaned_data['address']
            student.contact = form.cleaned_data['contact']
            student.email = form.cleaned_data['email']
            student.department = form.cleaned_data['department']
            student.semester = form.cleaned_data['semester']
            student.save()
            return HttpResponseRedirect('/Faculty/students')
    request.session['alert'] = None
    return render(request, 'Faculty/editstudent.html', {'student': student})


def delete_student(request, id):
    student = Students.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect('/Faculty/students')

def save_student(request):
    student = NewStudentForm(request.POST)

def lab(request):
    data = Lab.objects.filter(faculty=Faculty.objects.filter(loginid=Login.objects.get(pk=request.session['id']))[0])
    print(data)
    return render(request, 'Faculty/lab.html', {'labs': data})

def list_students(request, lab):
    data = Students.objects.all()
    print(data)
    return render(request, 'Faculty/labstudents.html', {'students': data, 'lab': lab})

def addexam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            lab = form.cleaned_data['lab']
            # semester = form.cleaned_data['semester']
            question1 = form.cleaned_data['question1']
            question2 = form.cleaned_data['question2']
            question3 = form.cleaned_data['question3']
            question4 = form.cleaned_data['question4']
            question5 = form.cleaned_data['question5']

            exam = Exam()
            exam.examname = name
            exam.date = date
            exam.lab = lab
            exam.time = time
            exam.semester = lab.semester
            exam.save()

            question = ExamQuestions()
            question.exam = exam
            question.question = question1
            question.save()

            question = ExamQuestions()
            question.exam = exam
            question.question = question2
            question.save()

            question = ExamQuestions()
            question.exam = exam
            question.question = question3
            question.save()

            question = ExamQuestions()
            question.exam = exam
            question.question = question4
            question.save()

            question = ExamQuestions()
            question.exam = exam
            question.question = question5
            question.save()

            students = Students.objects.filter(semester=lab.semester)
            for student in students:
                subject = lab.labname + " exam on " + date.strftime('%m/%d/%Y')
                body = lab.labname + " exam has been scheduled on " + date.strftime('%m/%d/%Y') + ", " + time.strftime('%H:%M') + ". You can login with exam_<registerno> as username ans exam as password"
                helpers.sendEmail(student.email, subject, body)

            examLogin = ExamLogin()

            for exam in ExamLogin.objects.all():
                exam.delete()

            examLogin.prefix = "exam"

    else:
        form = ExamForm()

    labs = Lab.objects.filter(faculty=Faculty.objects.filter(loginid=Login.objects.get(pk=request.session['id']))[0])

    exams = []
    for lab in labs:
        exam = Exam.objects.filter(lab=lab)
        if exam:
            for e in exam:
                exams.append(e)

    return render(request, 'Faculty/addexam.html', {'form': form, 'exams': exams})


def examstudents(request, examid):
    answers = []
    students = []
    for question in ExamQuestions.objects.filter(exam_id=examid):
        answerslist = ExamAnswers.objects.filter(examquestion=question)
        if answerslist:
            for answer in answerslist:
                answers.append(answer)
                students.append(Students.objects.filter(loginid=answer.loginid)[0].firstname)

    return render(request, 'Faculty/examstudents.html', {'answers': zip(answers, students)})


def examanswer(request, answerid):
    answer = ExamAnswers.objects.get(pk=answerid)
    file = open(answer.path, 'r')
    code = file.read()

    if request.method == 'POST':
        form = ExamMarksForm(request.POST)
        if form.is_valid():
            mark = form.cleaned_data['mark']
            total = form.cleaned_data['total']

            markobj = ExamMarks()
            markobj.mark = mark
            markobj.total = total
            markobj.examid = ExamQuestions.objects.get(pk=ExamAnswers.objects.get(pk=answerid).examquestion_id).exam
            markobj.login = ExamAnswers.objects.get(pk=answerid).loginid
            markobj.datetime = datetime.now()

            markobj.save()
    else:
        form = ExamMarksForm()

    return render(request, 'Faculty/examanswer.html', {'answer': answer, 'code': code, 'form': form})

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
    return render(request, 'Faculty/runprogram.html', {'lab': lab_object, 'stub': file.read(), 'programs': programs})


def handle_uploaded_file(f):
    uploaddir = os.path.join(settings.BASE_DIR, 'codepadapp/uploads')
    with open(os.path.join(uploaddir, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return os.path.join(uploaddir, f.name)

def exam(request):
    return render(request, 'Faculty/exam.html')
def contact(request):
    return render(request,'Faculty/contact.html')

def logout(request):
    Session.objects.all().delete()
    return HttpResponseRedirect('/')