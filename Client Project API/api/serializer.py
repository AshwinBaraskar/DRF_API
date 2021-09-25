from rest_framework import serializers
from .models import Client, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"
        # fields = ['id', 'client_name', 'created_at', 'created_by']
