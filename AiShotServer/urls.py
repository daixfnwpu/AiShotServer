"""AiShotServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from  AiShotServer.views.shotConfig import ShotConfigViewSet
from  AiShotServer.views.movie.ReviewViewSet import ReviewViewSet
from  AiShotServer.views.shop.ShopListView import ShopListView
from  AiShotServer.views.shop.FavoriteView import FavoriteViewSet
from  AiShotServer.views.shop.ProductView import ProductViewSet
from  AiShotServer.views.DeviceProfileViewSet import DeviceProfileViewSet
from .views.login import login_view
from .views.image_views import serve_image
from .views.auth_views import register_view
from .views.movie.movies import discover_movies, fetch_videos,fetch_reviews
from .views.fileupload_views import file_upload_view
from .views.wechat import views,urls
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views.user.user_views import UserAvatarUpdateView,UserAvatarViewSet
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from AiShotServer.views import wechat


# 创建路由器
router = DefaultRouter()
router.register(r'shotconfig', ShotConfigViewSet.ShotConfigViewSet, basename='shotconfig')
router.register(r'reviews', ReviewViewSet)
router.register(r'shops',ShopListView)
router.register(r'products', ProductViewSet)
router.register(r'favorite',FavoriteViewSet)
router.register(r'device/profile', DeviceProfileViewSet, basename='deviceprofile')
urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('images/<str:image_name>', serve_image, name='serve_image'),
    path('register/', register_view, name='register_view'),

    ## /discover/movie
    path('discover/movie/', discover_movies, name='discover_movies'),
    path('movie/<int:movie_id>/videos/', fetch_videos, name='fetch_videos'),
    path('movie/<int:movie_id>/reviews/', fetch_reviews, name='fetch_reviews'),
    path('upload/', file_upload_view, name='file_upload'),
    path('api/upload-avatar/', UserAvatarUpdateView.as_view(), name='upload-avatar'),
    path('api/user/<int:pk>/avatar/', UserAvatarViewSet.as_view({'get': 'retrieve'}), name='user-avatar'),

    # 包含 API 路由
    path('api/', include(router.urls)),
    path('wechat/', include(wechat.urls)),
   # path('shops/', ShopListView.as_view(), name='shop-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)