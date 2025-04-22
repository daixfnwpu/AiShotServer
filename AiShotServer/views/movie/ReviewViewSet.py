from rest_framework import viewsets
from ...models import Review
from ...serializers import ReviewSerializer
from .. import logger
"""
GET http://127.0.0.1:8000/reviews/：获取所有评论。
POST http://127.0.0.1:8000/reviews/：创建新的评论（需要提供 author, content, 和 url）。
GET http://127.0.0.1:8000/reviews/{id}/：获取特定评论的详细信息。
PUT/PATCH http://127.0.0.1:8000/reviews/{id}/：更新特定评论。
DELETE http://127.0.0.1:8000/reviews/{id}/：删除特定评论。

"""
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
