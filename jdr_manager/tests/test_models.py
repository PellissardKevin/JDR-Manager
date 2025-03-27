from django.test import TestCase
from jdr_manager.models import CharacterSheet, CustomUser, CharacterClass, Skill
from django.contrib.auth.models import User

class CharacterSheetModelTest(TestCase):
    def setUp(self):
        custom_user = CustomUser.objects.create(first_name="John", last_name="Doe")
        character_class = CharacterClass.objects.create(name="Guerrier", description="Un combattant robuste")
        skill = Skill.objects.create(name="Compétence de test", description="Une compétence pour tester")

        self.character_sheet = CharacterSheet.objects.create(
            user=custom_user,
            character_name="John le Guerrier",
            character_class=character_class,
            current_health=100,
            max_health=100,
        )
        self.character_sheet.skills.add(skill)

    def test_character_sheet_creation(self):
        self.assertEqual(self.character_sheet.character_name, "John le Guerrier")
        self.assertEqual(self.character_sheet.user.first_name, "John")
        self.assertEqual(self.character_sheet.skills.count(), 1)
