from django.contrib import admin
from .models import *


class BbAdmin(admin.ModelAdmin):
    fields = ('title', 'rubric', 'img', 'content', 'price', 'published')

    def get_readonly_fields(self, request, obj=None):
        f = ['published', ]
        if obj:
            f.append('rubric')
        return f

    list_display = ('title', 'rubric', 'content', 'price', 'published')
    list_display_links = ('title', 'rubric', 'content')
    search_fields = ('title', 'content')
    list_filter = ('title', 'rubric__name')
    view_on_site = True


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(SubRubric)
