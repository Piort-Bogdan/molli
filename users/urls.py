from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateView, PetCreateView
router = routers.SimpleRouter()
router.register(r'user', UserCreateView)
router.register(r'pet', PetCreateView)

urlpatterns = [
    # path('create-user/', views.UserCreateView.as_view(), name='create-user'),
    # path('create-pet/', views.PetCreateView.as_view(), name='create-pet'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]

urlpatterns = router.urls