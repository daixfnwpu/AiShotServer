from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from rest_framework_simplejwt.tokens import RefreshToken
from AiShotServer.models import CustomUser
import json
@csrf_exempt  # Exempt CSRF for simplicity in this example, but handle security properly in production
def login_view(request):
    if request.method == 'POST':
        try:
            appcode = request.POST.get('Pst_App_ID')
            username = request.POST.get('Pst_PhoneNum')
            password = request.POST.get('Pst_Password') 
            print("request data is : " + str(request.body))
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
              #  print(refresh)
              #  print(refresh.access_token)
                response_data = {
                    'LoginJSON':[
                           {'Pst_PhoneNum':user.username},
                           {'Pst_UserID':user.pk},
                           {'Pst_Password':user.password}  ### TODO ;为什么要写死这个密码呢？
                        
                        ],
                    'success': 1,
                    'message': 'Login successful',
                    'token' : str(refresh),
                    'access': str(refresh.access_token),
                    'userId' : user.pk
                    # 'user': {
                    #     'username': user.username,
                    #     'email': user.email,
                    # }
                }
            else:
                response_data = {
                    'success': 0,
                    'message': 'Invalid username or password'
                }
        except json.JSONDecodeError:
            response_data = {
                'success': 0,
                'message': 'Invalid JSON'
            }
        print(response_data) 
        return JsonResponse(response_data)
    
    return JsonResponse({
        'success': 0,
        'message': 'Only POST method is allowed'
    }, status=405)  # Method Not Allowed
