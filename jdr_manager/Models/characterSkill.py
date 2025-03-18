from django.db import models
from .character import CharacterSheet
from .skill import Skill

class CharacterSkill(models.Model):
    character = models.ForeignKey(CharacterSheet, on_delete=models.CASCADE, related_name="character_skills")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    mastery_level = models.IntegerField(default=1)  # Niveau de maîtrise

    def __str__(self):
        return f"{self.character.character_name} - {self.skill.name} (Mastery {self.mastery_level})"
