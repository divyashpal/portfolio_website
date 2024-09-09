from django.contrib import admin
from .models import Project,ProjectImage,Tag

# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display =(
        "title",
        "link"
    )
    inlines = [ProjectImageInline]
    search_field =("title", "description")
    list_filter = ("tags",) 
    
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_field = ("name",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectImage)

    
