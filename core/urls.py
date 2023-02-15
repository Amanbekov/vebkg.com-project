from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import(
    TokenObtainPairView,TokenRefreshView, TokenVerifyView
)


urlpatterns2 = [
    path('company/' ,include ('apps.company.urls')),
    path('event/' ,include ('apps.event.urls')),
    path('vacancy/' ,include ('apps.vacanci.urls')),
    path('video/' ,include ('apps.video.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path ('api/token/token/verify', TokenVerifyView.as_view(),name='token_verify'),
    # path('auth/', include('djoser.urls')),
    path('api/', include(urlpatterns2))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

