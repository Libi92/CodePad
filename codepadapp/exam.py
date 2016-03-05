import os
import datetime
import random

from django.contrib.sessions.models import Session
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from codepadapp.models import Exam, ExamQuestions, Login, Lab, UserPrograms, ExamAnswers, Students

__author__ = 'ammu'


def index(request):
    return render(request, 'exam/index.html')


def exam(request):
    semester = Students.objects.filter(admission_no=request.session['regno'])[0].semester
    exams = Exam.objects.filter(semester=semester)
    exams = list(exams)
    for exam in exams:
        start_time = datetime.datetime.combine(exam.date, exam.time)
        finish_time = start_time + datetime.timedelta(hours=3)

        print(start_time, datetime.datetime.now(), finish_time)
        if not start_time < datetime.datetime.now() < finish_time:
            exams.remove(exam)
    return render(request, 'exam/exam.html', {'exams': exams, 'count': len(exams)})

def labexam(request, examid):
    examobj = Exam.objects.get(pk=examid)
    questions = ExamQuestions.objects.filter(exam=examobj)
    question = questions[random.randint(0, len(questions))]
    return render(request, 'exam/labexam.html', {'exam': examobj, 'question':question})


def save_program(request):
    name = request.GET['name']
    code = request.GET['code']
    language = request.GET['language']
    question = request.GET['question']
    exam = request.GET['exam']
    id = request.session['regno']
    directory = os.path.join("codepadapp", "exam",str(exam), str(id), language)

    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join("codepadapp", "exam",str(exam), str(id), language, name + "." + language.lower())
    file = open(filepath, 'w+')
    file.write(code)
    file.close()

    login = Students.objects.filter(admission_no=id)[0].loginid

    answer = ExamAnswers()
    answer.name = name
    answer.loginid = login
    answer.examquestion = ExamQuestions.objects.get(pk=question)
    answer.datetime = datetime.datetime.now()
    answer.path = filepath
    answer.save()

    return HttpResponse("program saved")


def logout(request):
    Session.objects.all().delete()
    return HttpResponseRedirect('/')
