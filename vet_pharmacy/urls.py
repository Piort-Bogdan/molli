from django.urls import path
from rest_framework import routers

from .views import ManufacturerView, MedicamentView

router = routers.SimpleRouter()
router.register(r'medicament', MedicamentView)
router.register(r'manufacturer', MedicamentView)


urlpatterns = router.urls