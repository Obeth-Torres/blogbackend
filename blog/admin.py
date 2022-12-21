from django.contrib import admin
from .models import Post, Capitulo

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'publish', 'subject', )
    list_filter = ('subject', 'publish', 'author')
    search_fields = ('title', 'body')


@admin.register(Capitulo)
class CapAdmin(admin.ModelAdmin):
    list_display = ('cap_title', 'cap_body')
    list_filter = ('post',)
