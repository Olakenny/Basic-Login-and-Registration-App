from django.urls import path, include
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#    path('articles/', articleList, name='article-list'),
#    path('article/<str:pk>/', articleDetails, name='article-details'),


# ]


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    
    path('api/', include(router.urls)),
    
]