from django.db.models import fields
from rest_framework import serializers
from .models import Element
 
class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('name', 'img', 'summary')