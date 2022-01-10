from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import CustomUserViewSet, redirection_view
from crm.views import ClientViewSet, ContractViewSet, EventViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', redirection_view),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('api/login/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/v1/', include(router.urls))
]
