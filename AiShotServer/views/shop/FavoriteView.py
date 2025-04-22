from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ...models import Favorite
from ...serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]  # 确保用户已认证

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 将当前用户作为外键保存
