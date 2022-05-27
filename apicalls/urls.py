from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    # For Project related manipulation
    path('get-projects/<pk>',views.ProjectDetails.as_view(),name='projects'),  # Just for getting details about Project
    path('projects',views.ProjectAPICRUD.as_view(),name='projects'),        # For posting new Project
    path('project/<pk>',views.ProjectAPICRUD.as_view(),name='project-pk'),  # for performing Update and Delete
    path('all-projects',views.ProjectList.as_view(),name='all-project'),

    # For Section Related manipulation
    path('section',views.SectionAPICRUD.as_view(),name='section'),
    path('section/<pk>',views.SectionAPICRUD.as_view(),name='section'),

    # For Media related manipulation
    path('media',views.MediaContentAPICRUD.as_view(),name='media-content'),
    path('media/<pk>',views.MediaContentAPICRUD.as_view(),name='media-content'),

    # Without Authentication
    path('project-list',views.AllProjectList.as_view(),name='all-projects-detail'),
    path('single-project/<pk>',views.ProjectDetailsWithoutAuth.as_view(),name='single-project'),
    path('', views.index, name='index'),


    # For Art Education related links
    path('art-education/<pk>',views.AllArtProject.as_view(),name='all-art-project'),
    path('art-project-list',views.ArtProjectList.as_view(),name='art-project-list'),

    # For Blogging related links
    path('blog/<pk>',views.SingleBlog.as_view(),name='single-blog'),
    path('blog-detail/<pk>',views.SingleBlogDetail.as_view(),name='single-blog-detail'),
    path('create-blog',views.CreateBlog.as_view(),name='create-blog'),

    # For Blogging related links
    path('blog-section/<pk>',views.SingleBlogSection.as_view(),name='blog-section'),
    path('create-blog-section',views.CreateBlogSection.as_view(),name='create-blog-section'),


    # for media group sections
    path('media-group-create',views.CreateMediaGroupBlogSection.as_view(),name='media-group-create'),
    path('media-group-delete/<pk>',views.DeleteMediaGroupBlogSection.as_view(),name='media-group-delete'),

    # for about page contents
    path('about',views.GetAboutList.as_view(),name='about-contents'),

    # For Authentication related
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
