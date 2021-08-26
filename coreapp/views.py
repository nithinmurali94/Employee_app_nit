from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializers

# Create your views here.


class EmployeeView(APIView):

    permission_classes = (IsAuthenticated,) 

    #methods-Get
    def get(self, request):
        """This function isused to list all the information in Employee table  """
        transformers = Employee.objects.all()
        serializer = EmployeeSerializers(transformers, many=True)
        return Response(serializer.data)
    
        
