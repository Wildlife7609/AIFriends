from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from web.models.user import UserProfile
from django.contrib.auth.models import User

class GetUserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            return Response({
                'result': True,
                'msg': 'get user info success',
                'data': {
                    'user_id': request.user.id,
                    'username': request.user.username,
                    'photo': request.user.photo.url,
                    'profile': request.user.profile,
                }
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)