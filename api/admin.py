from django.contrib import admin
from .models import Credential, UserDetail

# Register your models here.
admin.site.register(Credential)
admin.site.register(UserDetail)
