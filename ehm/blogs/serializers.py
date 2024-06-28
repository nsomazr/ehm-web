from rest_framework import serializers
from .models import Blogs

class BlogsModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Blogs

        fields = ('heading', 'banner', 'highlight', 'content')