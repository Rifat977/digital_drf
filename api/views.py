from multiprocessing import context
from urllib import response
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from yaml import serialize
from .models import *
import api.serializers as api_ser
from rest_framework import status

# Create your views here.
class CategoryList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = Category.objects.all()
        serializer = api_ser.CategorySerializer(queryset, many=True, context = {'request':request})
        return Response({'data': serializer.data, }, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = api_ser.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = api_ser.CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = api_ser.CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubcategoryList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = Subcategory.objects.all()
        serializer = api_ser.SubategorySerializer(queryset, many=True, context = {'request':request})
        return Response({'data': serializer.data, }, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = api_ser.SubategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubcategoryDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Subcategory.objects.get(pk=pk)
        except Subcategory.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = api_ser.SubategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = api_ser.SubategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PersonList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = api_ser.PersonSerializer(persons, many=True, context = {'request':request})
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = api_ser.PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = api_ser.PersonSerializer(person)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = api_ser.PersonSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PersonSearch(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        persons = Person.objects.filter(name__icontains=request.data['search'])
        serializer = api_ser.PersonSerializer(persons, many=True, context = {'request':request})
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
            
class GetPersonByCategory(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        persons = Person.objects.filter(category=id)
        serializer = api_ser.PersonSerializer(persons, many=True, context={'request':request})
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

class PersonDetailWithSubCat(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, cat_id, sub_id, per_id, format=None):
        persons = Person.objects.filter(id=per_id)
        serializer = api_ser.PersonSerializer(persons, many=True, context={'request':request})
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

class PersonBySubCategory(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, cat_id, sub_id, format=None):
        persons = Person.objects.filter(sub_category=sub_id, category=cat_id)
        serializer = api_ser.PersonSerializer(persons, many=True, context={'request':request})
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
