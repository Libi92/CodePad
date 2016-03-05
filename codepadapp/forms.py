from django import forms
from codepadapp.models import Faculty, Lab


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(max_length=100, label='', widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'Password', 'class': 'form-control'}))


class AddStudentsForm(forms.Form):
    file = forms.FileField(label='Select Student data')


class LabForm(forms.Form):
    semoptions = (('1', 'Sem 1'), ('2', 'Sem 2'), ('3', 'Sem 3'), ('4', 'Sem 4'), ('5', 'Sem 5'), ('6', 'Sem 6'), ('7', 'Sem 7'), ('8', 'Sem 8'))
    languageoptions = (('C', 'C'), ('CPP', 'CPP'), ('Java', 'Java'))

    name = forms.CharField(max_length=100, label='Lab Name', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Lab Name', 'class': 'form-control'}))
    semester = forms.ChoiceField(choices=semoptions, label='Semester', widget=forms.Select(attrs={'required': 'true', 'class': 'form-control'}))
    language = forms.ChoiceField(choices=languageoptions, label='Language', widget=forms.Select(attrs={'required': 'true', 'class': 'form-control'}))
    faculty = forms.ModelChoiceField(queryset=Faculty.objects.all(), label='Faculty', widget=forms.Select(attrs={'required': 'true', 'class': 'form-control'}))


class FacultyForm(forms.Form):
    staffid = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Staff ID', 'class': 'form-control'}))
    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Name', 'class': 'form-control'}))
    designation = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Designation', 'class': 'form-control'}))
    email = forms.CharField(max_length=100, label='', widget=forms.EmailInput(attrs={'required': 'true', 'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Phone', 'class': 'form-control'}))


class NewStudentForm(forms.Form):
    admission_no = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Admission No', 'class': 'form-control'}))
    firstname = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'First Name', 'class': 'form-control'}))
    lastname = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Last Name', 'class': 'form-control'}))
    address = forms.CharField(max_length=100, label='', widget=forms.Textarea(attrs={'required': 'true', 'placeholder': 'Address', 'class': 'form-control'}))
    contact = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Phone', 'class': 'form-control'}))
    email = forms.CharField(max_length=100, label='', widget=forms.EmailInput(attrs={'required': 'true', 'placeholder': 'Email', 'class': 'form-control'}))
    department = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Department', 'class': 'form-control'}))
    semester = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Semester', 'class': 'form-control'}))


class ChangePasswordForm(forms.Form):
    currentpassword = forms.CharField(max_length=100, label='', widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'Current Password', 'class': 'form-control'}))
    newpassword = forms.CharField(max_length=100, label='', widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'New Password', 'class': 'form-control'}))
    confirmpassword = forms.CharField(max_length=100, label='', widget=forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'Confirm Password', 'class': 'form-control'}))


class ExamForm(forms.Form):
    name = forms.CharField(max_length=100, label='Exam Name', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Exam Name', 'class': 'form-control'}))
    date = forms.DateField(label="Date", widget=forms.DateInput(attrs={'required': 'true', 'placeholder': 'Date', 'class': 'form-control'}))
    time = forms.TimeField(label="Time", widget=forms.TimeInput(attrs={'required': 'true', 'placeholder': 'Time', 'class': 'form-control'}))
    lab = forms.ModelChoiceField(queryset=Lab.objects.all(), label='Lab', widget=forms.Select(attrs={'required': 'true', 'class': 'form-control'}))
    # semester = forms.CharField(max_length=100, label='Semester', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Semester', 'class': 'form-control'}))
    question1 = forms.CharField(max_length=100, label='Question 1', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Question 1', 'class': 'form-control'}))
    question2 = forms.CharField(max_length=100, label='Question 2', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Question 2', 'class': 'form-control'}))
    question3 = forms.CharField(max_length=100, label='Question 3', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Question 3', 'class': 'form-control'}))
    question4 = forms.CharField(max_length=100, label='Question 4', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Question 4', 'class': 'form-control'}))
    question5 = forms.CharField(max_length=100, label='Question 5', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Question 5', 'class': 'form-control'}))


class ExamMarksForm(forms.Form):
    mark = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Marks', 'class': 'form-control'}))
    total = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'Out of', 'class': 'form-control'}))