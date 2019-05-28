from rest_framework import routers
from manager.api.views import ReportViewSet


router = routers.SimpleRouter()
router.register(r'report', ReportViewSet, base_name='api-report')


urlpatterns = router.urls
