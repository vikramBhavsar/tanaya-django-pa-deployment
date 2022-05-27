from django.contrib import admin
from .models import ArtMediaContent,ArtProject,Blog,BlogSection,MediaGroupSection,Project,Section,MediaContent,About

# registering art models
admin.site.register(ArtProject)
admin.site.register(ArtMediaContent)

# registering blogs
admin.site.register(Blog)
admin.site.register(BlogSection)
admin.site.register(MediaGroupSection)

# for gallery page
admin.site.register(Project)
admin.site.register(Section)
admin.site.register(MediaContent)


# for about page
admin.site.register(About)

