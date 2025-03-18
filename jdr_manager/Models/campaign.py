from django.db import models
from .user import CustomUser

class Campaign(models.Model):
    creator = models.ForeignKey(CustomUser, related_name='created_campaigns', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    max_players = models.IntegerField(default=4)  # Nombre de joueurs, avec un max entre 2 et 8
    game_style = models.CharField(max_length=100, choices=[
        ('D&D', 'Dungeons & Dragons'),
        ('Cthulhu', 'Cthulhu'),
        ('Pathfinder', 'Pathfinder'),
        ('Other', 'Other')
    ])
    is_active = models.BooleanField(default=True)
    players = models.ManyToManyField(CustomUser, related_name='campaigns', blank=True)

    def __str__(self):
        return self.name
