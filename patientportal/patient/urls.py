from rest_framework import routers
from .api import PatientViewset

router = routers.DefaultRouter()
router.register('api/patients', PatientViewset, 'patients')

urlpatterns = router.urls
