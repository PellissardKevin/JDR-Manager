from django.db import models

class CharacterInventory(models.Model):
    character = models.ForeignKey('CharacterSheet', on_delete=models.CASCADE, related_name='inventories')
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Quantité d'objets

    def __str__(self):
        return f"{self.character.character_name} - {self.item.name} x{self.quantity}"

    def use_item(self):
        """Utilise un objet consommable et le retire si nécessaire"""
        if self.item.is_consumable:
            if self.quantity > 1:
                self.quantity -= 1
                self.save()
            else:
                self.delete()  # Supprime l'entrée si l'objet est entièrement consommé
