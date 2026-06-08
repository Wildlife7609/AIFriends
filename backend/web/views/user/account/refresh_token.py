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
            
            try:
                token = RefreshToken(refresh_token)
            except TokenError as e:
                return Response({'result': False, 'msg': str(e)}, status=401)
            
            access_token = str(token.access_token)
            
            response_data = {
                'result': True,
                'msg': 'Refresh token success.',
                'data': {
                    'access_token': access_token,
                }
            }
            
            response = Response(response_data)
            
            # SimpleJWT token rotation
            rotate_tokens = getattr(settings, 'SIMPLE_JWT', {}).get('ROTATE_REFRESH_TOKENS', False)
            if rotate_tokens:
                # Blacklist the old refresh token if blacklist is enabled
                blacklist_tokens = getattr(settings, 'SIMPLE_JWT', {}).get('BLACKLIST_AFTER_ROTATION', False)
                if blacklist_tokens:
                    try:
                        token.blacklist()
                    except (AttributeError, TokenError):
                        pass
                
                # Rotate refresh token
                token.set_jti()
                token.set_exp()
                token.set_iat()
                
                # Update the cookie with the new rotated refresh token
                response.set_cookie(
                    key='refresh_token',
                    value=str(token),
                    httponly=True,
                    samesite='Lax',
                    secure=False,
                    max_age=86400 * 7
                )
                
            return response
        except Exception as e:
            return Response({'result': False, 'msg': str(e)}, status=401)