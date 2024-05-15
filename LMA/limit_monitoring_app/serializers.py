from rest_framework import serializers
from .models import Criterias

class CriteriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterias
        fields = '__all__'
