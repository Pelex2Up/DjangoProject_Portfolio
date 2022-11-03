from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'technology']
    list_display_links = ['id', 'title']
    search_fields = ['title']


admin.site.register(Project, ProjectAdmin)
