from rest_framework import serializers
from .models import PLDModel
class PLDSerializer(serializers.ModelSerializer):
    # get_date = serializers.DateField()
    class Meta:
        model = PLDModel
        fields='__all__'
