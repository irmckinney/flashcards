
from django.db import models
from django.conf import settings


class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="decks"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()

    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name="flashcards"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]
