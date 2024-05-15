from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Criterias
from .serializers import CriteriasSerializer
# Create your views here.



# this view function is used to create a new criteria with respect to the userinput
class CreateCriteriaView(APIView):
    def post(self,request):
        data            = request.data
        serialized_data = CriteriasSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)



#this view will help the client to update the criterias
class CriteriasUpdateAPIView(APIView):
    def put(self,request,criteria_id):
        data = request.data
        criteria = Criterias.objects.get(id=criteria_id)
        serializer = CriteriasSerializer(criteria,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'update successfull'},status=status.HTTP_200_OK)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)



# this view helps to delete an existing criteria
class CriteriasDeleteAPIView(generics.DestroyAPIView):
    queryset = Criterias.objects.all()
    serializer_class = CriteriasSerializer
    lookup_url_kwarg = 'pk'



# this view displays all the existing criterias
class CriteriasListAPIView(generics.ListAPIView):
    queryset = Criterias.objects.all()
    serializer_class = CriteriasSerializer





