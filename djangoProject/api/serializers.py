from rest_framework import serializers


class ContSerializer(serializers.Serializer):
    urlpath = serializers.CharField()
    result = serializers.CharField()
