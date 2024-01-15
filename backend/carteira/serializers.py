from rest_framework import serializers

from carteira.models import Acao


class AcaoSerializer(serializers.Serializer):
    class Meta:
        model = Acao
        fields = '__all__'
