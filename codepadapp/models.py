from __future__ import unicode_literals
from _ast import mod
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.username


class Students(models.Model):
    loginid = models.ForeignKey(Login)
    admission_no = models.CharField(max_length=256)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    contact = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    department = models.CharField(max_length=256)
    semester = models.CharField(max_length=256)

    def __str__(self):
        return self.firstname


class Faculty(models.Model):
    loginid = models.ForeignKey(Login)
    staffid = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Lab(models.Model):
    labname = models.CharField(max_length=256)
    semester = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculty)

    def __str__(self):
        return self.labname

    def faculty_name(self):
        return self.faculty.name


class UserPrograms(models.Model):
    loginid = models.ForeignKey(Login)
    lab = models.ForeignKey(Lab)
    language = models.CharField(max_length=256)
    programname = models.CharField(max_length=256)
    date = models.DateTimeField()
    path = models.CharField(max_length=256)

    def __str__(self):
        return self.programname


class Exam(models.Model):
    examname = models.CharField(max_length=256)
    date = models.DateField()
    time = models.TimeField()
    lab = models.ForeignKey(Lab)
    semester = models.CharField(max_length=256)

    def __str__(self):
        return self.examname


class ExamQuestions(models.Model):
    question = models.CharField(max_length=1024)
    exam = models.ForeignKey(Exam)

    def __str__(self):
        return self.question


class ExamLogin(models.Model):
    prefix = models.CharField(max_length=256)


class ExamAnswers(models.Model):
    name = models.CharField(max_length=256)
    loginid = models.ForeignKey(Login)
    examquestion = models.ForeignKey(ExamQuestions)
    path = models.CharField(max_length=1024)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.examquestion.question


class ExamMarks(models.Model):
    login = models.ForeignKey(Login)
    examid = models.ForeignKey(Exam)
    mark = models.FloatField()
    total = models.FloatField()
    datetime =models.DateTimeField()