from rest_framework.routers import DefaultRouter
from mailgainer_app.views import UserViewSet



router = DefaultRouter()
router.register('user/', UserViewSet)

urlpatterns = router.urls

