from rest_framework.views import APIView
from blog.models import Article , Paragraph , Comment
from ..serializers.blog_serialzer import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#@api_view(["GET","POST"])
def get_all_article(request):
    if request.method == 'GET':
        blogs = Article.publish.all()
        
        serializer = BlogSerializer(blogs , many=True)
        
        return Response(data={"blogs":serializer.data},status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        
        data = request.POST 
        
        serializer = BlogSerializer(data= data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(data={"blog":serializer.initial_data})
        
        else:
            return Response(data={
                "errors" : serializer.errors
            })




class ListCreateBlog(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    
    
    def get(self,request, format = None):
        blogs = Article.publish.all()
        
        serializer = BlogSerializer(blogs , many=True)
        
        return Response(data={"blogs":serializer.data},status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        data = request.POST 
        
        serializer = BlogSerializer(data= data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(data={"blog":serializer.initial_data})
        
        else:
            return Response(data={
                "errors" : serializer.errors
            })