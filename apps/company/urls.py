from django.urls import path
from rest_framework.routers import DefaultRouter as DR
from apps.company.views import CompanyView


from apps.company.views import (
    CompanyView
)

router=DR()

router.register('company', CompanyView, basename= 'company')

urlpatterns=[]

urlpatterns += router.urls
