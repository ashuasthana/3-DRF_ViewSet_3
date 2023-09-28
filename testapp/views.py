from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NameSerializer

# Create your views here.
class TestViewSet(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        color=['red','blue','green']
        return Response({'msg':"Msg come From list method.",'colors':color})
    
    def create(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg=f"Hello {name},Data come from Create method."
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    
    def retrieve(self,request,pk=None,*args,**kwargs):
        msg=f"Hello, Data come from retrive method."
        return Response({'msg':msg})
    
    def update(self,request,pk=None,*args,**kwargs):
        msg=f"Hello, Data come from update method."
        return Response({'msg':msg})
    
    def partial_update(self,request,*args,**kwargs):
        msg=f"Hello, Data come from partical_update method."
        return Response({'msg':msg})
    
    def destroy(self,request,pk=None,*args,**kwargs):
        msg=f"Hello, Data come from destory method."
        return Response({'msg':msg})
