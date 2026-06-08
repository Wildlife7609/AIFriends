from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    permission_classes = [IsAuthenticated] #强制必须登录才能访问

    def post(self, request):
        try:
            response = Response({
                'result': True,
                'msg': 'Logout success.',
            })
            response.delete_cookie('refresh_token')
            return response
        except Exception as e:
            return Response({'result': False, 'msg': str(e)})

    