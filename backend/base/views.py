# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication

from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    




# class ArticleViewSet(viewsets.ViewSet):

#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         querryset = Article.objects.all()
#         article = get_object_or_404(querryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         article=Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# @authentication_classes((TokenAuthentication,))
# @permission_classes([IsAuthenticated])
# def articleList(request):

#     # get all articles

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # create an article

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def articleDetails(request,pk):

#     try:
#         article = Article.objects.get(pk=pk)
    
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article, many=False)
#         return Response(serializer.data, status=200)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
