from rest_framework import serializers

class MySerializer(serializers.Serializer):
    file = serializers.FileField()