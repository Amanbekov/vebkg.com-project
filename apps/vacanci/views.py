
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Vacancii
from .serializers import VacanciSerializer


class VakanciView(ModelViewSet):
    queryset = Vacancii.objects.all()
    serializer_class = VacanciSerializer
    permission_classes = (IsAuthenticated, )