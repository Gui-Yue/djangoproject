from django.contrib import admin

# Register your models here.
from square.models import Title
from square.models import Content
admin.site.register(Title)
admin.site.register(Content)