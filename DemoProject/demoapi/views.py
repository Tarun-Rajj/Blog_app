from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(http_method_names=['GET'])
def view_first_api(request):
    resp=Response(data="This is my FirstAPI")
    return resp

# Create your views here.
