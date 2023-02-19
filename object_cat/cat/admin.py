from django.contrib import admin

from .models import Cat, User

admin.site.register(Cat)
admin.site.register(User)