from django.contrib import admin

# Register your models here.
from .models import CharacterSheet, Campaign, Skill, Spell, CustomUser, GameTemplate, XpSystem, CharacterClass, CharacterSkill, CharacterXP, Damage

admin.site.register(CustomUser)
admin.site.register(GameTemplate)
admin.site.register(XpSystem)
admin.site.register(CharacterClass)
admin.site.register(CharacterSkill)
admin.site.register(CharacterXP)
admin.site.register(CharacterSheet)
admin.site.register(Campaign)
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(Damage)
