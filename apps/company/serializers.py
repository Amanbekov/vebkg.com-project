from rest_framework import serializers
from apps.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= Company
        fields=(
            'id', 'name','description','telegram',
            'logo','whatsapp', 'vacanci_amount',
            'event_amount', 'video_amount',
        )

