from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Star, Planet, Author

admin.site.register(Author)
admin.site.register(Star)
admin.site.register(Planet)


