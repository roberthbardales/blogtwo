from django.contrib import admin

# Register your models here.

from .models import Category,Tag,Posts,About,Link

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','active','created')
class TagAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','active','created')
class PostsAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display=('title','published','author','category','post_tags')
    ordering=['author','-created']
    search_fields=('title','content','author__username','category__name')
    list_filter=('author','category','tags')

    def post_tags(self,obj):
        return ' - '.join([t.name for t in obj.tags.all().order_by('name')])

    post_tags.short_description='Etiquetas'

class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('descripcion','created')

class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','key','url','icon')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Posts,PostsAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Link,LinkAdmin)