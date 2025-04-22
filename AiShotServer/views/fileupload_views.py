from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.files.storage import default_storage
from django.utils import timezone
from AiShotServer.models import Movie, Video
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
# 文件上传的保存路径
UPLOAD_DIR = 'media/uploads/'  # 确保这个文件夹存在

@api_view(['PUT','POST'])
@permission_classes([IsAuthenticated])  # 使用 JWT 认证
def file_upload_view(request):
    if request.method == 'POST':
        # 获取上传的文本字段
        description = request.POST.get('description')

        # 检查是否上传了图片
        image_files = request.FILES.getlist('images[]')
        video_file = request.FILES.get('video')
        current_time = timezone.now()
        current_user = request.user
        print(f" current user : {current_user}, {type(current_user)}")
        # 保存图片文件
        image_urls = []
        for image in image_files:
            image_name = default_storage.save(f'uploads/images/{image.name}', image)
            image_url = default_storage.url(image_name)
            image_urls.append(image_url)

        if len(image_urls) == 0 :
            image_urls=['uploads/images/defalut_img.png']
        # 保存视频文件
        video_url = None
        if video_file:
            video_name = default_storage.save(f'uploads/videos/{video_file.name}', video_file)
            video_url = default_storage.url(video_name)
        print(f"image_urls is {image_urls}")
        
        movie = Movie.objects.create(
            title=description,
            overview=description,
            release_date=current_time,
            poster_path=image_urls[0],
            backdrop_path = image_url[0],
            genre_ids = image_urls,  # Store genre IDs as a JSON array
            video=video_url,
            author = current_user.username)
        for image_url_ in image_urls:
            Video.objects.create(
            movie=movie,
            name=image_url_,
            site=image_url_,
            )
        
        # 返回上传的结果
        return JsonResponse({
            'description': description,
            'image_urls': image_urls,
            'video_url': video_url,
            'movie_id': movie.id,
            'author': current_user.username
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)
