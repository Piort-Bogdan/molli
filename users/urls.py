from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet, PetViewSet
router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'pet', PetViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]

urlpatterns = router.urls