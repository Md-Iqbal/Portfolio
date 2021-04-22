from django.contrib import admin
from .models import Personal_detail, CoCurricular_activity, Skill, Project, ContactMessage
# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'update_at', 'status']
    readonly_fields = ('name', 'email', 'subject', 'message', 'ip')
    list_filter = ['status']

admin.site.register(Personal_detail)
admin.site.register(CoCurricular_activity)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactMessage, ContactMessageAdmin)
