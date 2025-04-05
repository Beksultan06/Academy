from rest_framework.routers import DefaultRouter
from . views import ScientificJournalViewSet

router = DefaultRouter()
router.register(r'scientific-journals', ScientificJournalViewSet, basename='scientific-journal')
urlpatterns = router.urls
