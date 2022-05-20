"""rare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.db import router
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import register_user, login_user, PostView, CategoryView, CommentView, TagView, AuthorView, UserView, PhotoView
from rareapi.views.admin_view import AdminView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'comments', CommentView, 'comment')
router.register(r'categories', CategoryView, 'category')
router.register(r'posts', PostView, 'post')
router.register(r'tags', TagView, 'tag')
router.register(r'authors', AuthorView, 'author')
router.register(r'users', UserView, 'user')
router.register(r'admins', AdminView, 'admin')
router.register(r'photos', PhotoView, 'photo')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
