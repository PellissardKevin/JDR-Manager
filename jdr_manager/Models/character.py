from django.utils import timezone
from django.db import models
from .user import CustomUser
from .characterClass import CharacterClass
from .spell import Spell
from .skill import Skill
from .damage import Damage

class CharacterSheet(models.Model):
    user = models.ForeignKey(CustomUser, related_name='character_sheets', on_delete=models.CASCADE)
    character_name = models.CharField(max_length=255)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.SET_NULL, null=True, blank=True)
    race = models.CharField(max_length=100, blank=True, null=True)
    inventory = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    current_health = models.IntegerField()
    max_health = models.IntegerField()
    mana_points = models.IntegerField(default=100)
    skill_points = models.IntegerField(default=10)
    injuries = models.ManyToManyField('Damage', related_name='characters', blank=True)

    skills = models.ManyToManyField(Skill, related_name="character_sheets", blank=True)
    spells = models.ManyToManyField(Spell, related_name="characters", blank=True)

    def __str__(self):
        return f"{self.character_name} ({self.user.username})"

    def apply_injury(self, description, severity):
        # Créer une instance de Damage
        injury = Damage.objects.create(
            description=description,
            severity=severity
        )

        # Ajouter cette blessure à l'historique des blessures
        self.injuries.add(injury)

        # Appliquer la blessure aux points de vie
        self.current_health -= severity
        if self.current_health < 0:
            self.current_health = 0
        self.save()

