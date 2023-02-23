from django.contrib import admin
from . models import department,Role,Employee
# Register your models here.

admin.site.register(department)
admin.site.register(Role)
admin.site.register(Employee)