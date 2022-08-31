from rest_framework import serializers 
from djangularOperations.models import ArticleModel
 
 
class ArticleSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ArticleModel
        fields = ('id',
                  'title',
                  'description',
                  'published')