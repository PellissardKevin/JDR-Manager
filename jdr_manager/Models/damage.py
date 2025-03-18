from django.db import models

class Damage(models.Model):
    description = models.TextField()  # Description de la blessure
    severity = models.IntegerField()  # Gravité de la blessure
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - Severity {self.severity}"
