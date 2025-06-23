from rest_framework import serializers
from blog.models import Article , Paragraph , Comment

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ["title","image","mini_description","author","introduction","tags"]
    
    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return Article.objects.create(**validated_data)


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ["title","image","content"]