from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Modèle Utilisateur personnalisé
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    # Éviter les conflits avec Django
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True
    )

    def __str__(self):
        return self.username
