from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name field for our API testing"""
    name = serializers.CharField(max_length=10)