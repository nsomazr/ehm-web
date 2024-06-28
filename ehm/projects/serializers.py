from rest_framework import serializers
from .models import Projects

class ProjectsModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Projects

        fields = ('heading', 'banner', 'highlight', 'content')