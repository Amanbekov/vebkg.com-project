from rest_framework import serializers

from apps.vacanci.models import Vacancii


class VacanciSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vacancii
        fields=(
            'id','doljnost','oklad','type','description',
        )
        read_only_fields=('company',)