from rest_framework import serializers

#Create serializer 
class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=7)