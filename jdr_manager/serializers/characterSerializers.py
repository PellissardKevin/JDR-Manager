from rest_framework import serializers
from jdr_manager.models import CharacterSheet, CharacterXP, Damage, Skill, Spell, CustomUser, CharacterClass
from .damageSerializers import DamageSerializer
from .characterXpSerializer import CharacterXPSerializer

class CharacterSheetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    spells = serializers.PrimaryKeyRelatedField(queryset=Spell.objects.all(), many=True)
    character_class = serializers.PrimaryKeyRelatedField(queryset=CharacterClass.objects.all())
    injuries = DamageSerializer(many=True, required=False)

    # Ajouter CharacterXPSerializer pour la gestion de l'expérience
    xp = CharacterXPSerializer(required=False)  # Pour gérer l'XP du personnage, s'il y en a

    class Meta:
        model = CharacterSheet
        fields = '__all__'

    def create(self, validated_data):
        # Extraire les compétences, sorts et XP
        skills_data = validated_data.pop('skills', [])
        spells_data = validated_data.pop('spells', [])
        xp_data = validated_data.pop('xp', None)

        # Créer la fiche de personnage
        character_sheet = CharacterSheet.objects.create(**validated_data)

        # Associer les compétences
        for skill in skills_data:
            character_sheet.skills.add(skill)

        # Associer les sorts
        for spell in spells_data:
            character_sheet.spells.add(spell)

        # Créer et associer l'XP si fourni
        if xp_data:
            character_xp = CharacterXP.objects.create(character=character_sheet, **xp_data)
            character_sheet.xp = character_xp
            character_sheet.save()

        return character_sheet


