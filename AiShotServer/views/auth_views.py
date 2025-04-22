# myapp/views/auth_views.py

#from django.contrib.auth.models import User
from AiShotServer.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
          #  data = json.loads(request.body)
            username = request.POST.get('Pst_PhoneNum')
            password = request.POST.get('Pst_Password')
            ##!!!TODO !!! , use this phoneNum is email for user register;
            email = username+'@aishot.com'
            
            # Basic validation
            if not username or not password or not email:
                print(1)
                return JsonResponse({'message': 'All fields are required','success':0}, status=400)
            
            if CustomUser.objects.filter(username=username).exists():
                print(2)
                return JsonResponse({'message': 'Username already exists','success':210}, status=400)
            
            if CustomUser.objects.filter(email=email).exists():
                print(3)
                return JsonResponse({'message': 'Email already exists','success':0}, status=400)
            
            # Create the user
            user = CustomUser.objects.create(
                username=username,
                password=make_password(password),  # Hash the password before saving
                email=email
            )
            
            return JsonResponse({'message': 'User registered successfully','success':1}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data','success':0}, status=400)
    
    return JsonResponse({'message': 'Only POST requests are allowed','success':0}, status=405)
