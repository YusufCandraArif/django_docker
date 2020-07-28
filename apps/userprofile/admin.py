from django.contrib import admin

from .models import Profile, Follow


#semua yang ada hubungannya dengan admin/dashboard ada disini
# Register your models here.
admin.site.register(Profile)
admin.site.register(Follow)