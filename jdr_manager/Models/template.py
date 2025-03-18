from django.db import models

class GameTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stats_template = models.JSONField()

    def __str__(self):
        return self.name
