from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    effects = models.TextField(blank=True, null=True)  # Effets optionnels
    is_consumable = models.BooleanField(default=False)  # Si l'objet peut être consommé

    def __str__(self):
        return self.name
