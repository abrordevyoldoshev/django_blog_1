# ------- Bu korinishda adminga panelga kiritib olamiz
# ------- keyin views.py ga kirib views yaratamiz

from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)

