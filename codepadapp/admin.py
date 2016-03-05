from django.contrib import admin

# Register your models here.
from codepadapp.models import Login, Students, Lab, Faculty, UserPrograms, Exam, ExamAnswers, ExamQuestions, ExamMarks


class LoginAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'type']


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['admission_no', 'firstname', 'lastname', 'address', 'contact', 'email', 'department', 'semester']


class LabAdmin(admin.ModelAdmin):
    list_display = ['labname', 'semester', 'language', 'faculty_name']


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['loginid', 'staffid', 'name','email','designation','phone']


class ExamAdmin(admin.ModelAdmin):
    list_display = ['examname', 'date', 'time', 'lab']

class ExamAnswerAdmin(admin.ModelAdmin):
    list_display = ['loginid', 'examquestion', 'path', 'datetime']

admin.site.register(Login, LoginAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(UserPrograms)
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamAnswers, ExamAnswerAdmin)
admin.site.register(ExamQuestions)
admin.site.register(ExamMarks)