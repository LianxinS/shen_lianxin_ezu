from django.contrib import admin

from .models import Semester, Section, Student, Course, Instructor, Registration, Period, Year

admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Registration)
admin.site.register(Period)
admin.site.register(Year)
