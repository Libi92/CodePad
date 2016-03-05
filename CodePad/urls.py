"""CodePad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from codepadapp import views, codepadadmin, students, faculty, exam
import codepadapp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index',views.index, name='index'),
    url(r'^contact',views.contact, name='contact'),

    url(r'^about', views.about, name='about'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^index', views.home, name="home") ,
    url(r'^Admin/home', codepadadmin.index, name='admin'),
    url(r'^Admin/lab', codepadadmin.lab, name='lab'),
    url(r'^Admin/Faculty', codepadadmin.faculty, name='Faculty'),
    url(r'^Admin/logout', codepadadmin.logout, name='logout'),
    url(r'^Admin/exam',codepadadmin.exam,name='exam'),
    url(r'^Admin/contact',codepadadmin.contact,name='contact'),
    #url(r'^Admin/Faculty', codepadadmin.faculties, name='Faculties'),
    url(r'^Admin/editfaculty/(?P<id>\w+)/', codepadadmin.edit_Faculty, name='editfacultys'),
    url(r'^Admin/deletefaculty/(?P<id>\w+)/', codepadadmin.delete_Faculty, name='deletefacultys'),

    url(r'^Student/home', students.index, name='student'),
    url(r'^Student/lab', students.lab, name='lab'),
    url(r'^Student/runprogram/(?P<lab>\w+)/', students.runprogram, name='runprogram'),
    url(r'^Student/exec', students.execprogram, name='exec'),
    url(r'^Student/downloadprogram/(?P<name>\w+)/(?P<program>\w+)/', students.downloadprogram, name='download'),
    url(r'^Student/saveprogram', students.save_program, name='save'),
    url(r'^Student/getsavedprograms', students.get_saved_programs, name='savedprograms'),
    url(r'Student/exam',students.exam, name='exam'),
    url(r'Student/contact',students.contact, name='contact'),
    url(r'^Student/logout', students.logout, name='logout'),

    url(r'^Faculty/home', faculty.index, name='faculty'),
    url(r'^Faculty/lab', faculty.lab, name='lab'),
    url(r'^Faculty/liststudents/(?P<lab>\w+)/', faculty.list_students, name='labstudents'),
    url(r'^Faculty/runprogram/(?P<lab>\w+)/', faculty.runprogram, name='runprogram'),
    url(r'^Faculty/students', faculty.students, name='students'),url(r'^Faculty/home', faculty.index, name='faculty'),
    url(r'^Faculty/newstudent', faculty.new_student, name='newstudents'),
    url(r'^Faculty/editstudent/(?P<id>\w+)/', faculty.edit_student, name='editstudents'),
    url(r'^Faculty/deletestudent/(?P<id>\w+)/', faculty.delete_student, name='deletestudents'),
    url(r'^Faculty/contact',faculty.contact, name='contact'),
    url(r'^Faculty/exam',faculty.exam, name='exam'),
    url(r'^Faculty/addexam',faculty.addexam, name='addexam'),
    url(r'^Faculty/lexamstudents/(?P<examid>\w+)/', faculty.examstudents, name='examstudents'),
    url(r'^Faculty/eanswers/(?P<answerid>\w+)/', faculty.examanswer, name='examanswers'),
    url(r'^Faculty/logout', faculty.logout, name='logout'),

    url(r'^Exam/home', exam.index, name='exam'),
    url(r'^Exam/exam', exam.exam, name='exams'),
    url(r'^Exam/labexam/(?P<examid>\w+)/', exam.labexam, name='labexam'),
    url(r'^Exam/saveprogram', exam.save_program, name='save'),
    url(r'^Exam/logout', exam.logout, name='logout'),
]
