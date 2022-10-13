from django.contrib import admin
from .models import Category, Post, Comment

#for configuration
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description', 'url', 'add_date')
    search_fields = ('title', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat')
    search_fields = ('title',)
    list_filter = ('cat', )
    list_per_page = 5


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)