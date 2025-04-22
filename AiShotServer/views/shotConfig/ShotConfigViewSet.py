import logging
from rest_framework import viewsets
from rest_framework.response import Response
from ...models import ShotConfig
from ...serializers import ShotConfigSerializer
from rest_framework.exceptions import NotFound
from rest_framework import status
logger = logging.getLogger(__name__)
class ShotConfigViewSet(viewsets.ModelViewSet):
    queryset = ShotConfig.objects.all()
    serializer_class = ShotConfigSerializer

    # def list(self, request):
    #     """获取当前用户的所有配置"""
    #     queryset = ShotConfig.objects.filter(user=request.user)  # 只获取当前用户的配置
    #     serializer = ShotConfigSerializer(queryset, many=True)
    #     return Response({'configs': serializer.data})
    
    def list(self, request):
        """获取当前用户的所有配置，支持通过 isalreadyDown 参数过滤"""
        queryset = ShotConfig.objects.filter(user=request.user)
        
        # 获取查询参数 isalreadyDown
        isalready_down = request.query_params.get('isalreadyDown')
        
        if isalready_down is not None:
            queryset = queryset.filter(isalreadyDown=isalready_down)

        serializer = ShotConfigSerializer(queryset, many=True)
        return Response({'configs': serializer.data})
    def retrieve(self, request, pk=None):
        try:
            # 通过主键 (ID) 获取实例
            shot_config = self.get_object()  # 获取对象
            serializer = self.get_serializer(shot_config)  # 序列化
            return Response(serializer.data)  # 返回序列化数据
        except ShotConfig.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    def create(self, request):
        """为当前用户添加配置"""
        print(request.data)
        serializer = ShotConfigSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is ok!!")
            # 将当前用户设置为ShotConfig的user
            shot_config = serializer.save(user=request.user)
            return Response({'success': True, 'message': 'Config added successfully', 'configUI_id': shot_config.configUI_id}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'success': False, 'errors': serializer.errors}, status=400)

    def update(self, request, pk=None):
        """更新配置"""
        try:
            logger.debug(f" have inter the update method{pk}")
            shot_config = ShotConfig.objects.get(pk=pk, user=request.user)  # 确保只能更新当前用户的配置
        except ShotConfig.DoesNotExist:
            return Response({'success': False, 'message': 'Config not found'}, status=404)

        serializer = ShotConfigSerializer(shot_config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Config updated successfully'})
        logger.debug("update shotconfig %s", serializer.error_messages)
        return Response({'success': False, 'errors': serializer.errors}, status=400)

    def destroy(self, request, *args, **kwargs):
        try:
            shot_config = self.get_object()
            if shot_config.user != request.user:
                return Response({"error": "You do not have permission to delete this config."}, status=status.HTTP_403_FORBIDDEN)
            shot_config.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response({"error": "ShotConfig not found."}, status=status.HTTP_404_NOT_FOUND)
