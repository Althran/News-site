from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentList, ContactList


router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentList)
router.register(r'contacts', ContactList)


urlpatterns = [
    path('', include(router.urls)),
]
