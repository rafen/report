from rest_framework import routers
from report.api.views import ReportViewSet


router = routers.SimpleRouter()
router.register(r'report', ReportViewSet, base_name='api-report')


urlpatterns = router.urls
