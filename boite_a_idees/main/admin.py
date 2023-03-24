from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from idea.models import Idea

admin.site.register(User, UserAdmin)
admin.site.register(Idea)