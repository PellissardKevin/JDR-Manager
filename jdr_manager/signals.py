from django.db.models.signals import post_save
from django.dispatch import receiver
from jdr_manager.models import CharacterXP

@receiver(post_save, sender=CharacterXP)
def auto_update_level(sender, instance, **kwargs):
    instance.update_level_from_xp()
