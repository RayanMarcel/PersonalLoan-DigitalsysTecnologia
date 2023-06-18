from .views import ProposalViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'proposals', ProposalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]