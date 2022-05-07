from django.contrib import admin
from .models import Space, Post, Comment
# Register your models here.

admin.site.register(Space)
admin.site.register(Post)
admin.site.register(Comment)