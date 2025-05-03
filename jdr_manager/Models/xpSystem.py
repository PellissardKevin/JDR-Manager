from django.db import models
from .campaign import Campaign

class XpSystem(models.Model):
    PROGRESSION_CHOICES = [
        ("slow", "Lent"),
        ("medium", "Moyen"),
        ('fast', "Rapide"),
    ]

    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE, related_name="xp_system")
    level_cap = models.IntegerField(default=20)  # Maximum de niveaux
    xp_formula = models.TextField(blank=True, null=True)  # Si tu veux une formule custom
    progression_type = models.CharField(max_length=10, choices=PROGRESSION_CHOICES, default="medium")

    def __str__(self):
        return f"XP System for {self.campaign.name}"

    def generate_xp_table(self):
        speed_multipliers = {
            "slow": 1.5,
            "medium": 1.0,
            "fast": 0.7,
        }

        multiplier = speed_multipliers.get(self.progression_type, 1.0)
        base_xp = 100
        xp_table = ()

        for level in range(1, self.level_cap + 1):
            xp_required = int((level ** 2.2) * base_xp * multiplier)
            xp_table[level] = xp_required

        return xp_table
