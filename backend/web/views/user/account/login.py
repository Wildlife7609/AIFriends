from rest_framework_simplejwt.tokens import RefreshToken
from web.models import UserProfile
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    def post(self, request, *arg, **kwargs):
        try:
            username = request.data.get('username').strip()
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({'result': False, 'msg': 'username or password is null.'})
            user = authenticate(username=username, password=password)
            if user:
                user_profile = UserProfile.objects.get(user__username=username)
                refrs_token = RefreshToken.for_user(user)
                response = Response({
                    'result': True,
                    'msg': 'Login success.',
                    'data': {
                        'access_token': str(refrs_token.access_token),
                        'user_id': user.id,
                        'username': user.get_username(),
                        'photo': user_profile.photo.url if user_profile.photo else '',
                        'profile': user_profile.profile,
                    }
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refrs_token),
                    httponly=True,
                    samesite='Lax',
                    secure=False,
                    max_age=86400 * 7
                )
                return response
            return Response({'result': False, 'msg': 'Invalid username or password.'})
        except Exception as e:
            return Response({'result': False, 'msg': str(e)})
