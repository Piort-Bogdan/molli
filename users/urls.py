from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views


urlpatterns = [
    path('create-user/', views.UserCreateView.as_view(), name='create-user'),
    path('create-pet/', views.PetCreateView.as_view(), name='create-pet'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]
