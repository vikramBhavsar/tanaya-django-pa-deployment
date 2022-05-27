from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import About, ArtMediaContent, ArtProject, Project,Section,MediaContent,Blog, BlogSection, MediaGroupSection

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class MediaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContent
        fields = "__all__"    

class SectionMainSerializer(serializers.ModelSerializer):
    mediaContent = MediaContentSerializer(many=True,read_only=True)

    class Meta:
        model = Section
        fields = "__all__"


class ProjectMainSerializer(serializers.ModelSerializer):

    sections = SectionMainSerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


##### For Art Section

# this is used for Isolated
class ArtProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtProject
        fields = "__all__"

# this is used for Isolated
class ArtMediaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtMediaContent
        fields = "__all__"

## This is used for combined Data
class ArtProjectMainSerializer(serializers.ModelSerializer):
    art_media = ArtMediaContentSerializer(many=True,read_only=True)

    class Meta:
        model = ArtProject
        fields = "__all__"


################# SERIALIZERS FOR BLOG PART

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = "__all__"

class MediaGroupSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaGroupSection
        fields = "__all__"    


class BlogSectionMainSerializer(serializers.ModelSerializer):
    media_group_section = MediaGroupSectionSerializer(many=True,read_only=True)
    class Meta:
        model = BlogSection
        fields = "__all__"

class BlogMainSerializer(serializers.ModelSerializer):

    blog_sections = BlogSectionMainSerializer(many=True,read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"   


