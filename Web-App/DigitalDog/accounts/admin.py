from django.contrib import admin
from django.contrib.auth.decorators import login_required


# Register your models here.

admin.site.login = login_required(admin.site.login)
