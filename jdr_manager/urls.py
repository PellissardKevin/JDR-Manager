from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jdr_manager.views import (
    CustomUserViewSet,
    GameTemplateViewSet,
    CharacterClassViewSet,
    CharacterSkillViewSet,
    CharacterXPViewSet,
    SkillViewSet,
    SpellViewSet,
    XpSystemViewSet,
    CharacterSheetViewSet,
    CampaignViewSet,
    DamageViewSet,
    ItemViewSet,
    CharacterInventoryViewSet
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'game-templates', GameTemplateViewSet)
router.register(r'character-classes', CharacterClassViewSet)
router.register(r'character-skills', CharacterSkillViewSet)
router.register(r'character-xp', CharacterXPViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'spells', SpellViewSet)
router.register(r'xp-systems', XpSystemViewSet)
router.register(r'character-sheets', CharacterSheetViewSet)
router.register(r'campaigns', CampaignViewSet)
router.register(r'damages', DamageViewSet)
router.register(r'items', ItemViewSet)
router.register(r'character-inventories', CharacterInventoryViewSet)

# Ajout des routes générées automatiquement par le router
urlpatterns = [
    path('', include(router.urls)),
]
