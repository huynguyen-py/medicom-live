from django.contrib import admin
from .models import Comment, Post, Category
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['id']

    class Meta:
        models = Post


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'date']
    list_filter = ['date']
    search_fields = ['post']

    class Meta:
        models = Comment


admin.site.register(Category)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Post, PostModelAdmin)

