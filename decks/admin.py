
from django.contrib import admin
from .models import Deck, Flashcard


class FlashcardInline(admin.TabularInline):
    model = Flashcard
    extra = 1


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "description", "owner__username")
    readonly_fields = ("created_at",)
    inlines = [FlashcardInline]


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ("question", "deck", "created_at")
    list_filter = ("created_at", "deck")
    search_fields = ("question", "answer", "deck__title")
    readonly_fields = ("created_at",)
