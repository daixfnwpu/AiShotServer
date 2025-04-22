from rest_framework import serializers

from .models import DeviceProfile, Favorite, InitialRubberLength, Review, RubberProfile, RubberThickness, RubberWidth, Shop, Video,Movie,Product
from .models import ShotConfig
from AiShotServer.models import CustomUser


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all_'
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'name', 'site', 'key', 'size', 'type']

                
class ShotConfigSerializer(serializers.ModelSerializer):
    device_profile = 'DeviceProfileSerializer()'  # 通过嵌套序列化器返回 DeviceProfile 详情
    user = serializers.SlugRelatedField(slug_field='id', queryset=CustomUser.objects.all())
    class Meta:
        model = ShotConfig
        fields = [
            'configUI_id', 
            'user', 
            'device_profile', 
            'radius_mm', 
            'humidity', 
            'crossofrubber', 
            'Cd', 
            'airrho', 
            'initvelocity', 
            'pellet', 
            'eyeToBowDistance', 
            'eyeToAxisDistance', 
            'altitude', 
            'isalreadyDown'
        ]        
class ReviewSerializer(serializers.ModelSerializer):
    ### TODO: 用这个来实现外键的关联；
    user = serializers.SlugRelatedField(slug_field='id', queryset=CustomUser.objects.all())
    movie = serializers.SlugRelatedField(slug_field='id', queryset=Movie.objects.all())
    class Meta:
        model = Review
        fields = ['id', 'author', 'content', 'url','user','movie']
        
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'  # 或者指定特定字段，如 ['id', 'name', ...]
        
    
    

class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['avatar']
    # 将 avatar 字段重写为只读字段，并返回图片的 URL
    avatar = serializers.SerializerMethodField()
    
    def get_avatar(self, obj):
        request = self.context.get('request')
        if obj.avatar and hasattr(obj.avatar, 'url'):
            return request.build_absolute_uri(obj.avatar.url)
        return None
    
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # 包含所有字段
        
        
class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # 嵌套 ProductSerializer，以返回产品详细信息
    user_id = serializers.IntegerField(source='user.id', read_only=True)  # 只读字段，返回用户 ID

    class Meta:
        model = Favorite
        fields = ['id', 'user_id', 'product', 'created_at']  # 包含所需的字段

    def create(self, validated_data):
        user = validated_data.pop('user')  # 从验证数据中提取用户信息
        favorite = Favorite.objects.create(user=user, **validated_data)  # 创建 Favorite 实例
        return favorite
    
    


        

class RubberThicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubberThickness
        fields = ['thickness']

class InitialRubberLengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialRubberLength
        fields = ['length']

class RubberWidthSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubberWidth
        fields = ['width']

class RubberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubberProfile
        fields = ['rubber_thickness', 'initial_rubber_length', 'rubber_width']
        
class DeviceProfileSerializer(serializers.ModelSerializer):
    thinofrubber_mm = serializers.CharField(source='RubberThickness.thickness')  # 假设有一个 value 字段
    initlengthofrubber_m = serializers.CharField(source='InitialRubberLength.length')
    widthofrubber_mm = serializers.CharField(source='RubberWidth.width')

    class Meta:
        model = DeviceProfile
        fields = ['model', 'shotDoorWidth', 'shotHeadWidth', 'wifi_account', 'wifi_password', 'ble_connection', 'battery_level', 'thinofrubber_mm', 'initlengthofrubber_m', 'widthofrubber_mm']
