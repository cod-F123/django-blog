from django.contrib import admin
from .models import Article , Paragraph , Comment

# Register your models here.


class InlineParagraph(admin.StackedInline):
    model = Paragraph
    extra = 1


class InlineComment(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "status", "date_created"]
    list_filter = ["status", "date_created"]
    search_fields = ["title", "author__username", "tags"]
    readonly_fields = ["date_created", "date_updated","slug"]
    inlines = [InlineParagraph,InlineComment]

admin.site.register(Paragraph)
admin.site.register(Comment)