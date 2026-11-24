
from django.contrib import admin
from .models import StudyProgress


@admin.register(StudyProgress)
class StudyProgressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "flashcard",
        "is_known",
        "review_count",
        "last_reviewed",
        "next_review",
    )

    list_filter = (
        "is_known",
        "last_reviewed",
        "next_review",
    )

    search_fields = (
        "user__username",
        "flashcard__question",
        "flashcard__deck__title",
    )
