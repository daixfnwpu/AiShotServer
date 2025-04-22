from rest_framework import generics, permissions, parsers
from ...model.user.CustomUser import UserAvatarSerializer
from ...model.user.CustomUser import CustomUser
from rest_framework.response import Response
from rest_framework import viewsets
import logging

logger = logging.getLogger(__name__)


### uplaod dictory is : /media/avatars
class UserAvatarUpdateView(generics.UpdateAPIView):
    serializer_class = UserAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]  # 确保用户已登录
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    def get_object(self):
        return self.request.user  # 获取当前用户
    def get_serializer_context(self):
        return {'request': self.request}  # 将 request 传递给序列化器上下文


class UserAvatarViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        logger.debug(f"the pk is : {pk}")
        print(f"the pk is : {pk}")
        user = CustomUser.objects.get(pk=pk)
        serializer = UserAvatarSerializer(user)
        logger.debug(serializer.data)
        print(f"ser.data is : {serializer.data}")

        return Response(serializer.data)