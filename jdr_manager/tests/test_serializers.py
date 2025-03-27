from rest_framework.test import APITestCase
from jdr_manager.models import CustomUser, CharacterSheet, Skill
from jdr_manager.serializers import CharacterSheetSerializer
from django.contrib.auth.models import User


class CharacterSheetSerializerTest(APITestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(username="test_user", password="test_password")
        character_sheet = CharacterSheet.objects.create(
            user=user,
            character_name="John le Guerrier",
            character_class=None,  # Exemple simplifié
            current_health=100,
            max_health=100,
        )
        skill = Skill.objects.create(name="Compétence de test", description="Une compétence pour tester")
        character_sheet.skills.add(skill)
        self.character_sheet = character_sheet

    def test_character_sheet_serializer(self):
        serializer = CharacterSheetSerializer(self.character_sheet)
        self.assertEqual(serializer.data['character_name'], "John le Guerrier")
        self.assertEqual(serializer.data['skills'][0], self.character_sheet.skills.first().id)
