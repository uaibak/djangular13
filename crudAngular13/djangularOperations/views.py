from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from djangularOperations.models import ArticleModel
from djangularOperations.serializers import ArticleSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def article_list(request):
    if request.method == 'GET':
        articles = ArticleModel.objects.all()
        title = request.query_params.get('title', None)

        if title is not None:
            articles = articles.filter(title__icontains=title)

        articles_serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(articles_serializer.data, safe=False)

    elif request.method == 'POST':
        article_data = JSONParser().parse(request)
        articles_serializer = ArticleSerializer(data = article_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse(articles_serializer.data, status =status.HTTP_201_CREATED)
        return JsonResponse(articles_serializer.errors, status = status.HTTP_404_NOT_FOUND)

    elif(request.method == 'DELETE'):
        count = ArticleModel.objects.all().delete()
        return JsonResponse({'message': 'Article deleted successfully'.format(count[0])}, status =status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try: 
        article = ArticleModel.objects.get(pk=pk) 
    except ArticleModel.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        article_serializer = ArticleSerializer(article) 
        return JsonResponse(article_serializer.data) 
 
    elif request.method == 'PUT': 
        article_data = JSONParser().parse(request) 
        article_serializer = ArticleSerializer(article, data=article_data) 
        if article_serializer.is_valid(): 
            article_serializer.save() 
            return JsonResponse(article_serializer.data) 
        return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        article.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def article_list_published(request):
    articles = ArticleModel.objects.filter(published=True)
        
    if request.method == 'GET': 
        article_serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(article_serializer.data, safe=False)