from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('book_title', 'author', 'rating', 'created_at')
	list_filter = ('rating', 'created_at', 'author')
	search_fields = ('book_title', 'author__username', 'text')
