from rest_framework import viewsets
from ..models import DeviceProfile, InitialRubberLength, RubberProfile, RubberThickness, RubberWidth
from ..serializers import DeviceProfileSerializer
from rest_framework.permissions import IsAuthenticated

class DeviceProfileViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 获取外键实例
        rubber_thickness = RubberThickness.objects.get(value=self.request.data['thinofrubber_mm'])
        initial_rubber_length = InitialRubberLength.objects.get(length=self.request.data['initlengthofrubber_m'])
        rubber_width = RubberWidth.objects.get(width=self.request.data['widthofrubber_mm'])

        # 保存 DeviceProfile 并关联外键
        serializer.save(
            user=self.request.user,  # 假设你有当前用户
            thinofrubber_mm=rubber_thickness,
            initlengthofrubber_m=initial_rubber_length,
            widthofrubber_mm=rubber_width
        )
        
    def perform_update(self, serializer):
        # 获取外键实例
        rubber_thickness = RubberThickness.objects.get(value=self.request.data['thinofrubber_mm'])
        initial_rubber_length = InitialRubberLength.objects.get(length=self.request.data['initlengthofrubber_m'])
        rubber_width = RubberWidth.objects.get(width=self.request.data['widthofrubber_mm'])

        # 更新 DeviceProfile 并关联外键
        serializer.save(
            thinofrubber_mm=rubber_thickness,
            initlengthofrubber_m=initial_rubber_length,
            widthofrubber_mm=rubber_width
        )
        
    def get_queryset(self):
        # 获取当前用户
        user = self.request.user
        device_profiles = DeviceProfile.objects.filter(user=user)
        
        # 如果用户没有设备配置文件，创建默认的 DeviceProfile 和 RubberProfile
        if not device_profiles.exists():
            # 创建默认的 DeviceProfile
            device_profile = DeviceProfile.objects.create(user=user)
            
            # 为该设备配置文件创建默认的 RubberProfile
            RubberProfile.objects.create(
                device_profile=device_profile,
                rubber_thickness=0.0045,  # 设置默认的 rubber_thickness
                initial_rubber_length=0.22,  # 设置默认的 initial_rubber_length
                rubber_width=0.025  # 设置默认的 rubber_width
            )
            
            # 重新获取用户的设备配置文件
            device_profiles = DeviceProfile.objects.filter(user=user)

        return device_profiles
