from rest_framework.routers import DefaultRouter

from marketplace.viewsets import DelayReportViewSet, OrderViewSet, TripViewSet, VendorViewSet


router = DefaultRouter()

router.register('vendors', VendorViewSet, basename='vendors')
router.register('orders', OrderViewSet, basename='orders')
router.register('trips', TripViewSet, basename='trips')
router.register('delay-reports', DelayReportViewSet, basename='delay-reports')
