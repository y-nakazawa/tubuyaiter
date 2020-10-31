from django.contrib import admin
from app.models import Mutter


class MutterAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at_to_str')
    search_fields = ['content']

    def created_at_to_str(self, obj):
        return obj.created_at.strftime('%Y/%m/%d %H:%M:%S')

    created_at_to_str.short_description = 'つぶやいた日時'


admin.site.register(Mutter, admin_class=MutterAdmin)
