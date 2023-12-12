from django.db import models

# Create your models here.
class students(models.Model):  # creating models.Model ,it is the inheritance same as oops concept
    student_ID = models.IntegerField()
    student_name = models.CharField(max_length = 50)
    course = models.CharField(max_length = 30)
    jdate = models.DateField()
    def __str__(self):          # str is structure
        return self.student_name   # row will be displayed by name student_name


