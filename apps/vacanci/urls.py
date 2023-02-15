from django.urls import path
from rest_framework.routers import DefaultRouter as DR
from apps.vacanci.views import VakanciView


from apps.vacanci.views import (
    VakanciView
)

router=DR()

router.register('vakanci', VakanciView, basename= 'vakanci')

urlpatterns=[]

urlpatterns += router.urls