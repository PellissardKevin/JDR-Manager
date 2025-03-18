from django.db import models

class Spell(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    mana_cost = models.IntegerField(default=0)
    required_spells = models.ManyToManyField("self", symmetrical=False, blank=True)  # Prérequis
    spell_level = models.IntegerField(default=1)  # Niveau du sort

    def __str__(self):
        return f"{self.name} (Coût : {self.mana_cost} mana, Niveau {self.spell_level})"
