from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({'result': False, 'msg': 'refresh_token is null.'}, status=401)
            
            token = RefreshToken(refresh_token)
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                token.set_jti()
                response = Response({
                    'result': True, 
                    'msg': 'Refresh token success.', 
                    'access': str(token.access_token)
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(token),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7
                )
                return response
            return Response({
                    'result': True, 
                    'msg': 'success but no need to rotate the token.', 
                    'access': str(token.access_token)
                })
        except Exception as e:
            return Response({'result': False, 'msg': str(e)}, status=401)