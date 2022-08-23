from django.contrib import admin
from .models import User, IAMUser

admin.site.register(User)
admin.site.register(IAMUser)
