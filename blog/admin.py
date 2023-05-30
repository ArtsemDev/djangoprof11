from django.contrib import admin

from .models import Category, Post, Contact


class PostStackedInline(admin.StackedInline):
    model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    # list_editable = ('slug', )
    search_fields = ('name', 'slug')
    search_help_text = 'Название или URL'
    empty_value_display = 'Н/У'
    # readonly_fields = ('slug', )
    prepopulated_fields = {'slug': ('name', )}
    inlines = (PostStackedInline, )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
