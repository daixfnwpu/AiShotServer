from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import json
from rest_framework_simplejwt.tokens import AccessToken

class MyAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 打印请求方法、URL 和头信息
        print(f"Request Method: {request.method}")
        print(f"Request URL: {request.build_absolute_uri()}")
        print(f"Request Headers: {dict(request.headers)}")
        print(f"Request body:{request.body}") 
        # 如果请求有数据，尝试打印数据内容
        """   if request.body:
            try:
                print(f"Request Body: {json.loads(request.body)}")
            except json.JSONDecodeError:
                print(f"Request Body: {request.body}") """
        try:
            response = self.get_response(request)
        except Exception as e:
            print(f" exception is : {e}")
        if response.get('Content-Type') == 'application/json':
            try:
                # 解析并打印JSON内容
                response_content = json.loads(response.content)
                print(f"Response JSON content: {json.dumps(response_content, indent=4)}")
            except json.JSONDecodeError:
                print("Response content is not valid JSON.")
        else:
            print(f"Response content: {response}")

        print(f"Response status code: {response.status_code}")
        return response
    def verify_token(self,token_str):
        try:
            token = AccessToken(token_str)  # 解析 Token
            return token
        except Exception as e:
            print("Token 无效:", e)
            return None