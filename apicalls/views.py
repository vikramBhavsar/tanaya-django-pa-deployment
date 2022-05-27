from ast import Delete
from json import JSONDecoder
from urllib import response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import MultiPartParser,JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, mixins, generics
from .serializers import AboutSerializer, ArtProjectMainSerializer, BlogMainSerializer, BlogSectionSerializer, BlogSerializer, ProjectSerializer, MediaContentSerializer, SectionSerializer,ProjectMainSerializer,MediaGroupSectionSerializer
from .models import About, ArtProject, Blog, BlogSection, MediaContent, MediaGroupSection, Project,Section


# Create your views here.
def index(request):
    return HttpResponse("hello World")

# CRUD operation for Project models - ( ONLY AUTHENTICATED )
class  ProjectAPICRUD(generics.ListAPIView, mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer
    permission_classes = [IsAuthenticated]

    # get new Project
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # for Creating a new project
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    # for updating an existing project
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # for deleting an existing project
    def delete(self, request, *args, **kwargs):
        print("Inside destroy method %s" % kwargs)
        return self.destroy(request,*args,**kwargs)

class ProjectDetails(generics.ListAPIView, mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer
    permission_classes = [IsAuthenticated]

    # get new Project
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

# CRD operation for MediaContent Model
class MediaContentAPICRUD(generics.ListAPIView,mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    parser_classes = [MultiPartParser,JSONParser]
    serializer_class = MediaContentSerializer
    queryset = MediaContent.objects.all()
    permission_classes = [IsAuthenticated]

    # getting existing section details
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)

# CRUD operations for Section Model
class SectionAPICRUD(generics.ListAPIView, mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]

    # getting existing section details
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Creating new project
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    # updating existing project
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # deleting existing project
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)

# This view will show all the data combined, includes projects, sections and media content
class AllDataList(generics.ListAPIView,mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer

# This view will show all the data combined, includes projects, sections and media content
class AllProjectList(generics.ListAPIView,mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# This view will show all data combined for Single Project (Without Authentication)
class ProjectDetailsWithoutAuth(generics.ListAPIView, mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectMainSerializer

    # get new Project
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)




#########################################################
#########################################################
# BELOW WILL CONTAIN ART EDUCATION VIEWS
#########################################################
#########################################################

class AllArtProject(generics.ListAPIView,mixins.RetrieveModelMixin):
    queryset = ArtProject.objects.all()
    serializer_class = ArtProjectMainSerializer

    # get new Project
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ArtProjectList(generics.ListAPIView):
    queryset = ArtProject.objects.all()
    serializer_class = ProjectSerializer



#########################################################
#########################################################
# BELOW WILL CONTAIN BLOGGING RELATED VIEWS
#########################################################
#########################################################


### for parent main blog
class SingleBlog(generics.ListAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    # get blog
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # deleting existing blog
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)

class CreateBlog(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    # Creating new blog
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


#### FOR sections inside blog
class SingleBlogSection(generics.ListAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer
    permission_classes = [IsAuthenticated]

    # get blog
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # updating existing blog section
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # deleting existing blog
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)


class GetBlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreateBlogSection(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer
    permission_classes = [IsAuthenticated]

    # Creating new blog
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


class CreateBlogSection(generics.ListAPIView, mixins.CreateModelMixin):
    parser_classes = [MultiPartParser,JSONParser]
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer
    permission_classes = [IsAuthenticated]

    # Creating new blog
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


class CreateMediaGroupBlogSection(generics.ListAPIView, mixins.CreateModelMixin):
    parser_classes = [MultiPartParser,JSONParser]
    queryset = MediaGroupSection.objects.all()
    serializer_class = MediaGroupSectionSerializer
    permission_classes = [IsAuthenticated]

    # Creating new blog
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


class DeleteMediaGroupBlogSection(generics.ListAPIView, mixins.DestroyModelMixin):
    queryset = MediaGroupSection.objects.all()
    serializer_class = MediaGroupSectionSerializer
    permission_classes = [IsAuthenticated]

    def delete(self,request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)


# Getting detail information about the blog
class SingleBlogDetail(generics.ListAPIView,mixins.RetrieveModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogMainSerializer

    # get blog
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)




### misceleenius
class GetAboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer