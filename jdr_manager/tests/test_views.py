from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from jdr_manager.models import CustomUser, CharacterSheet, CharacterClass
from rest_framework import status

class CharacterSheetViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Créer un utilisateur (CustomUser)
        self.user = CustomUser.objects.create(username="test_user", password="test_password")

        # Supprime les objets existants pour éviter les conflits de clé unique
        CharacterClass.objects.filter(name="Guerrier").delete()

        # Créer une classe de personnage (optionnelle, si nécessaire)
        self.character_class = CharacterClass.objects.create(name="Guerrier", description="Un combattant robuste")

        # Créer une fiche personnage (CharacterSheet)
        self.character_sheet = CharacterSheet.objects.create(
            user=self.user,
            character_name="John le Guerrier",
            character_class=self.character_class,
            current_health=100,
            max_health=100,
        )

        # Authentifie l'utilisateur pour les tests
        self.client.force_authenticate(user=self.user)

        # L'URL de la vue
        self.url = reverse('charactersheet-list')

    def test_character_sheet_list(self):
        # Test de la liste des fiches personnage
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_create_character_sheet(self):
        # Vérifie si le CharacterClass existe déjà
        character_class, created = CharacterClass.objects.get_or_create(name="Guerrier", description="Un combattant robuste")

        data = {
            "user": self.character_sheet.user.id,
            "character_name": "Test Character",
            "character_class": character_class.id,
            "current_health": 100,
            "max_health": 100,
            "skills": [],  # Liste vide pour les compétences
            "spells": [],   # Liste vide pour les sorts
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['character_name'], 'Test Character')

