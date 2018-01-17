from django.contrib import admin

# Register your models here.
from testApp.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Post, PostAdmin)
