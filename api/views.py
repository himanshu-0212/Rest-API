from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Element
from .serializers import ElementSerializer
from django.shortcuts import get_object_or_404
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_elements': '/',
        'Search by Category': '/?category=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': 'element/delete/pk'
    } 
    return Response(api_urls)

@api_view(['POST'])

# create

def add_elements(request):
    element = ElementSerializer(data=request.data)
 
    if Element.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if element.is_valid():
        element.save()
        return Response(element.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Read

@api_view(['GET'])
def view_elements(request):

    if request.query_params:
        elements = Element.objects.filter(**request.query_params.dict())
    else:
        elements = Element.objects.all()
 
    if elements:
        serializer = ElementSerializer(elements, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Update 

@api_view(['POST'])
def update_elements(request, pk): 
    element = Element.objects.get(pk=pk)
    data = ElementSerializer(instance=element, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Delete

@api_view(['DELETE'])
def delete_elements(request, pk):
    element = get_object_or_404(Element, pk=pk)
    element.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
