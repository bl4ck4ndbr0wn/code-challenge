from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .renderers import MultipleJSONRenderer


class RetrieveMultiplesAPIView(APIView):
    """
    Handles if the integer is:
    ■ a multiple of 5, it should return "L"
    ■ a multiple of 7, it should return "R"
    ■ a multiple of both 5 and 7, then both "LR" should be displayed
    """
    renderer_classes = (MultipleJSONRenderer,)

    def get(self, request):
        """
        Handles check if argument is a multiple of 5 or 7
        :param kwargs:
        :return: { data: string, message: string}
        """
        data = int(request.query_params.get('number', ''))

        if isinstance(data, int):
            data = "L"*(not data % 5) + "R"*(not data % 7) or data

        return Response(data, status=status.HTTP_200_OK)
