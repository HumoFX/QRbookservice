from django.contrib import admin
from .models import Article, Comment, Books, Categories


# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("books_name",)}


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Books, BooksAdmin)
admin.site.register(Categories)

