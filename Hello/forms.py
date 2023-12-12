from django import forms

# class studentform(forms.Form):
#     student_ID = forms.IntegerField()
#     student_name = forms.CharField()
#     course = forms.CharField()
#     jdate = forms.DateField()

# creating a form using models
from django.forms import ModelForm                             # 10
from Hello.models import students                              # 10.1

class studentform(ModelForm):                                  # 10.2
    class Meta:
        model = students    # students is the  class name that created in models
        # fields = 'all'   (or)  we can import all the fields or else we can use all
        fields = ['student_ID','student_name', 'course', 'jdate']
        labels={'student_ID':'ID','student_name':'name','course':'course','jdate':'joiningdate'}

form = studentform()