from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView



class GetUsers(APIView):
    def get(self, request):
        msg = 'i am here'
        return Response(msg)