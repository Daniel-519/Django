from django.contrib import admin
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_authors', 'review', 'date_reviewed', 'is_favourite')
    fieldsets = [
        ("Book Details", {"fields": ["title", 'authors']}),
        ("Review", {"fields": ["is_favourite", "review", "date_reviewed"]})
    ]
    readonly_fields = ['date_reviewed']

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = "Author(s)"

    list_editable = ("is_favourite", )
    list_display_links = ('title', 'date_reviewed',)
    list_filter = ('is_favourite',)
    search_fields = ('title', )


admin.site.register(Book, BookAdmin)
admin.site.register(Author)


