from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if refresh_token:
                try:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                except Exception:
                    # Ignore if token is already blacklisted/expired or blacklist app not enabled
                    pass

            response = Response({
                'result': True,
                'msg': 'Logout success.',
            })
            response.delete_cookie('refresh_token')
            return response
        except Exception as e:
            return Response({'result': False, 'msg': str(e)})

    