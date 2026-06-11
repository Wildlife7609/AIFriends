from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from web.models.user import UserProfile
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username').strip()
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({'result': False, 'msg': 'username or password is null.'})
            if User.objects.filter(username=username).exists():
                return Response({'result': False, 'msg': 'username is already exists.'})

            # 创建用户
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.get(user=user)
            refresh_token = RefreshToken.for_user(user) 
            response = Response({
                'result': True,
                'msg': 'Register success.',
                'data': {
                    'access_token': str(refresh_token.access_token),
                    'user_id': user.id,
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.profile,
                }
            })
            response.set_cookie(
                key='refresh_token',
                value=str(refresh_token),
                httponly=True,
                samesite='Lax',
                secure=False,
                max_age=86400 * 7
            )
            return response
        except Exception as e:
            return Response({'result': False, 'msg': str(e)})