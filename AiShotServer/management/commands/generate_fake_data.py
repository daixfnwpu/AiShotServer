from django.core.management.base import BaseCommand
from faker import Faker
import random
from AiShotServer.models import CustomUser, DeviceProfile, Favorite, Product, Review, Shop, ShotConfig  # 替换为你自己的应用名和模型

# 使用 Faker 库生成随机数据
faker = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for Review and Shop models'

    def handle(self, *args, **kwargs):

        for _ in range(10):
            user = CustomUser.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password='password123'  # 使用固定密码或随机生成
            )
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
            
        for _ in range(5):
            product = Product.objects.create(
                title=faker.catch_phrase(),
                image_url=faker.image_url(),
                price=faker.random_number(digits=2),
                description=faker.text(max_nb_chars=200),
                rating=faker.random_int(min=1, max=5),
                is_on_sale=faker.boolean(),
                sale_price=faker.random_number(digits=2),
                sales_count=faker.random_int(min=1, max=100)
                )
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.title}'))

                # 创建假收藏
            Favorite.objects.create(user=user, product=product)
            self.stdout.write(self.style.SUCCESS(f'Created favorite for user: {user.username} and product: {product.title}'))
            
        for _ in range(10):
            device_profile = DeviceProfile.objects.create(
                model=faker.random_element(elements=["铂金版", "黄金版", "白银版"]),
                bow_gate_distance=faker.pyfloat(left_digits=1, right_digits=2, positive=True, min_value=0.03, max_value=0.06),
                head_width=faker.pyfloat(left_digits=1, right_digits=3, positive=True, min_value=0.02, max_value=0.03),
                rubber_thickness=faker.pyfloat(left_digits=1, right_digits=4, positive=True, min_value=0.004, max_value=0.005),
                initial_rubber_length=faker.pyfloat(left_digits=1, right_digits=2, positive=True, min_value=0.2, max_value=0.25),
                rubber_width=faker.random_element(elements=[0.025, 0.03]),
                wifi_account=faker.user_name(),  # 生成随机 Wi-Fi 账号
                wifi_password=faker.password(),  # 生成随机 Wi-Fi 密码
                ble_connection=faker.boolean(),  # 随机生成布尔值
                battery_level=faker.random_int(min=50, max=100)  # 电量在 50% 到 100% 随机生成
            )
            self.stdout.write(self.style.SUCCESS(f'Created DeviceProfile: {device_profile.model}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data!'))