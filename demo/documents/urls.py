from rest_framework import routers

from .views import DocumentViewSet

router = routers.SimpleRouter()
router.register(r"documents", DocumentViewSet)
urlpatterns = router.urls
