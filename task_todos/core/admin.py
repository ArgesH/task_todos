from django.contrib import admin
from core.models import Photo, Manager, Director, Employee

# Register your models here.

admin.site.register(Photo)
admin.site.register(Manager)
admin.site.register(Director)
admin.site.register(Employee)
