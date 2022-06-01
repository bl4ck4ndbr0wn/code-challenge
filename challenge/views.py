from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions

from .renderers import MultipleJSONRenderer
import re

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
        # data = int(request.query_params.get('number', ''))

        num = request.GET.get('number' , None)
        # check if number parameter was entered.
        if num is None:
            return Response({'errors': "User Input is required."}, status=status.HTTP_400_BAD_REQUEST)

        # check if number parameter is a valid integer.
        result  = re.match("[-+]?\d+$", num)
        if result is None:
            return Response({'errors': "User Input must be an integer"}, status=status.HTTP_400_BAD_REQUEST)
        # check if num is a multiple of 5 or 7 or both else return the number
        s = int(num)
        data = "L"*(not s % 5) + "R"*(not s % 7) or s

        return Response(data, status=status.HTTP_200_OK)
