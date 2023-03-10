from django.urls import path

from .views import registration


urlpatterns = [
    path('registration/', registration.as_view())

]