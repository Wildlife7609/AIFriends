from rest_framework_simplejwt.tokens import RefreshToken
from web.models.user import UserProfile
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response



class LoginView(APIView):
    def post(self, request, *arg, **kwargs):
        try:
            username = request.data.get('username').strip()
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({'result': False, 'msg': 'username or password is null.'})
            
            user = authenticate(username=username, password=password)
            if user:
                user_profile = UserProfile.objects.get(user=user)
                refresh = RefreshToken.for_user(user) # generate access token and refresh token
                response = Response({
                    'result': True,
                    'msg': 'Login success.',
                    'data': {
                        'access_token': str(refresh.access_token),
                        'user_id': user.id,
                        # pyrefly: ignore [missing-attribute]
                        'username': user.username,
                        'photo': user_profile.photo.url,
                        'profile': user_profile.profile,
                    }
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=False,
                    max_age=86400 * 7
                )
                return response
            return Response({'result': False, 'msg': 'Invalid username or password.'})
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return Response({'result': False, 'msg': str(e)})
