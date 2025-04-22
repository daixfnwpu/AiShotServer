import requests
from django.http import JsonResponse

# 替换为你的微信AppID和AppSecret
WECHAT_APPID = 'your_wechat_appid'
WECHAT_SECRET = 'your_wechat_secret'

def wechat_login(request):
    code = request.POST.get('code')
    
    if not code:
        return JsonResponse({'status': 'error', 'message': 'Code is missing'}, status=400)
    
    try:
        # 获取微信 access_token
        access_token, openid = get_wechat_access_token(code)
        # 获取微信用户信息
        user_info = get_wechat_user_info(access_token, openid)
        # 处理用户登录逻辑
        user = handle_user_login(user_info)
        return JsonResponse({'status': 'success', 'user': user})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def get_wechat_access_token(code):
    url = f"https://api.weixin.qq.com/sns/oauth2/access_token?appid={WECHAT_APPID}&secret={WECHAT_SECRET}&code={code}&grant_type=authorization_code"
    response = requests.get(url)
    data = response.json()
    
    if 'access_token' in data:
        return data['access_token'], data['openid']
    else:
        raise Exception("Failed to get access_token: " + data.get('errmsg', 'Unknown error'))

def get_wechat_user_info(access_token, openid):
    url = f"https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}"
    response = requests.get(url)
    return response.json()

def handle_user_login(user_info):
    openid = user_info['openid']
    # 假设数据库查找用户的逻辑
    user = find_user_by_openid(openid)
    
    if user:
        return user
    else:
        # 用户不存在，注册新用户
        return register_new_user(user_info)

def find_user_by_openid(openid):
    # 模拟查询数据库
    return None  # 假设用户不存在

def register_new_user(user_info):
    # 模拟注册逻辑
    return {"openid": user_info['openid'], "nickname": user_info['nickname'], "status": "new"}
