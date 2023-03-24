from rest_framework import routers

from appointment.views import AppointmentView, ReceptionView

router = routers.SimpleRouter()
router.register(r'appointment', AppointmentView)
router.register(r'reception', ReceptionView)
urlpatterns = [

]

urlpatterns += router.urls