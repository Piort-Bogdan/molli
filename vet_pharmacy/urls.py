from django.urls import path
from rest_framework import routers

from .views import ManufacturerViewSet, MedicamentViewSet

router = routers.SimpleRouter()
router.register(r'medicament', MedicamentViewSet)
router.register(r'manufacturer', MedicamentViewSet)


urlpatterns = router.urls