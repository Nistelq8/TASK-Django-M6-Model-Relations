from django.contrib import admin

from classes import models

to_register = [
    models.Lecture,
    models.Slide,
    models.Course
]

admin.site.register(to_register)
