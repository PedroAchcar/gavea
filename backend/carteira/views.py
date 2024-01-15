from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

from carteira.models import Acao
from carteira.serializers import AcaoSerializer


class AcaoApiView(APIView):
    def post(self, request):
        serializer = AcaoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'acao': serializer.data,
                'status': HTTP_201_CREATED
            })
        return Response({
            'message': serializer.errors,
            'status': HTTP_400_BAD_REQUEST
        })

    def get(self, request):
        acoes = Acao.objects.all()
        serializer = AcaoSerializer(acoes, many=True)

        return Response({
            'acoes': serializer.data,
            'status': HTTP_200_OK
        })
