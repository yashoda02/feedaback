from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message_preview', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)

    def message_preview(self, obj):
        return obj.message[:20] + "..."  # Shows only first 50 characters
    message_preview.short_description = "Message Preview"
