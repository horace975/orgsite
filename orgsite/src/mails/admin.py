from django.contrib import admin

# Register your models here.
from mails.models import LeaveMessage

class LeaveMessageAdmin(admin.ModelAdmin):
	list_display = ('created_at', 'name', 'email', 'content',)
	search_fields = ('email',)

admin.site.register(LeaveMessage, LeaveMessageAdmin)
