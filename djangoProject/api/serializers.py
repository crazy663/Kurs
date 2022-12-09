from rest_framework import serializers

class ContSerializer(serializers.Serializer):
    url = serializers.CharField()
    result = serializers.CharField()