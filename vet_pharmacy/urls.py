from django.urls import path
from .views import ManufacturerAddView, MedicamentAddView


urlpatterns = [
    path('manufacturer/', ManufacturerAddView.as_view()),
    path('medicament/', MedicamentAddView.as_view(), name='medicament')

]