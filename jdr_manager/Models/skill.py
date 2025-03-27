from django.db import models
from .template import GameTemplate

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    game_template = models.ForeignKey(GameTemplate, on_delete=models.CASCADE, related_name="skills", null=True, blank=True)
    requires_level = models.IntegerField(default=0)  # Niveau minimum requis
    skill_level = models.IntegerField(default=1)  # Niveau de compétence

    def __str__(self):
        return f"{self.name} (Lvl {self.skill_level})"
