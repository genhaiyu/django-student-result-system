from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone


# Create your models here.
class Class(models.Model):
    level = models.CharField(max_length=250)
    section = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.level + ' - ' + self.section)


class Subject(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    classI = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')), default=1)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id + " - " + self.first_name + " " + (
            str(self.middle_name + " " + self.last_name) if self.middle_name != '' else self.last_name))

    def get_name(self):
        return str(self.first_name + " " + (
            str(self.middle_name + " " + self.last_name) if self.middle_name != '' else self.last_name))


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.semester}"

    def count_subjects(self):
        try:
            result_count = StudentSubjectResult.objects.filter(result=self).count()
        except:
            result_count = 0
        return result_count

    def average(self):
        average = 0
        try:
            result_count = StudentSubjectResult.objects.filter(result=self).count()
            results = StudentSubjectResult.objects.filter(result=self).aggregate(Sum('grade'))['grade__sum']
            if results is not None:
                average = results / result_count
        except Exception as err:
            print(err)
        return average


class StudentSubjectResult(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.FloatField(default=0)

    def __str__(self):
        return f"{self.result} - {self.subject}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contact = models.CharField(max_length=250)
    dob = models.DateField()
    address = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/')

    def __str__(self):
        return self.user.username
