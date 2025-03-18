from django.db import models
from .character import CharacterSheet

class CharacterXP(models.Model):
    character = models.OneToOneField(CharacterSheet, on_delete=models.CASCADE, related_name="xp")
    level = models.IntegerField(default=1)
    current_xp = models.IntegerField(default=0)

    def add_xp(self, amount):
        self.current_xp += amount
        # Ici logique de montée de niveau
        self.save()

    def __str__(self):
        return f"{self.character.character_name} - Level {self.level} ({self.current_xp} XP)"
