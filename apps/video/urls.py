
from rest_framework.routers import DefaultRouter as DR
from apps.video.views import VideoView

router=DR()

router.register('video',VideoView, basename= 'video')

urlpatterns=[]

urlpatterns += router.urls