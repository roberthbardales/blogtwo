from django.contrib import admin

# Register your models here.

from .models import Category,Tag,Posts

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','active','created')
class TagAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','active','created')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Posts)