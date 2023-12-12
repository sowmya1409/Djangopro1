from django.contrib import admin

# Register your models here.
from .models import students            #steps  1. makemigration
admin.site.register(students)                   #2. migrate
                                                #3. run server
