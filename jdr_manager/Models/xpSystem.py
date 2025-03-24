from django.db import models
from .campaign import Campaign

class XpSystem(models.Model):
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE, related_name="xp_system")
    level_cap = models.IntegerField(default=20)  # Maximum de niveaux
    xp_formula = models.TextField(blank=True, null=True)  # Pour stocker une formule d'XP spécifique

    def __str__(self):
        return f"XP System for {self.campaign.name}"
