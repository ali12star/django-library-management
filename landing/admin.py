from django.contrib import admin
from .models import ContactMessage , Book

@admin.register(ContactMessage)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created')
    search_fields = ('name', 'email', 'subject')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'created')
    search_fields = ('title', 'author')