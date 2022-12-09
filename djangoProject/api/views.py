from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cont
from .serializers import ContSerializer
from func_app.func import get_html


class ContView(APIView):
    def get(self, request, url):
        content = Cont(url, get_html(url))

        serializer_for_request = ContSerializer(instance=content)
        return Response(serializer_for_request.data)


