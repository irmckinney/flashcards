
from django.db import models
from django.conf import settings


class StudyProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="study_progress"
    )

    flashcard = models.ForeignKey(
        "decks.Flashcard",
        on_delete=models.CASCADE,
        related_name="study_progress"
    )

    last_reviewed = models.DateTimeField(null=True, blank=True)
    next_review = models.DateTimeField(null=True, blank=True)
    review_count = models.PositiveIntegerField(default=0)
    is_known = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "flashcard"],
                name="unique_user_flashcard_progress"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.flashcard}"
