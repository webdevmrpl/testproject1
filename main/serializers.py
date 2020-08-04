from rest_framework.serializers import ModelSerializer
from .models import Rubric


class RubricSerializer(ModelSerializer):
    class Meta:
        model = Rubric
        fields = ('id', 'name')
