from django.db import models
from .skill import Skill
from .spell import Spell

class CharacterClass(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    available_skills = models.ManyToManyField(Skill, blank=True)
    available_spells = models.ManyToManyField(Spell, blank=True)

    def __str__(self):
        return self.name
