from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repositories.post_repository import get_all_posts

class PostListView(APIView):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 8))

        try:
            posts = get_all_posts(page, limit)
            return Response({
                "message": "posts_list_success",
                "data": {
                    "posts": posts
                }
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print("게시글 로드 오류:", e)
            return Response({"message": "internal_server_error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
