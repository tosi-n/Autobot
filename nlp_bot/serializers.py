from rest_framework import serializers
from .models import Bitron


class BitronSerializer(serializers.ModelSerializer):
    # lft = serializers.SlugRelatedField(slug_field='lft', read_only=True)
    class Meta:
        model = Bitron
        fields = "__all__"