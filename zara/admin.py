from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Parent)
admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(PhotoGallery)
