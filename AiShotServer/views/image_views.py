# myapp/views/image_views.py

from django.http import FileResponse, HttpResponseNotFound
import os

def serve_image(request, image_name):
    # Define the path to the directory containing images
    image_dir = os.path.join(os.path.dirname(__file__), '..\\..\\media')
    print(image_dir)
    image_path = os.path.join(image_dir, image_name)
    print(image_path)
    if os.path.exists(image_path):
        # Return the image as a file response
        response = FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{image_name}"'
        return response
    else:
        return HttpResponseNotFound('Image not found')