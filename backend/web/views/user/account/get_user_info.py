from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from web.models.user import UserProfile
from django.contrib.auth.models import User

class GetUserInfoView(APIView):
    # Allow guests to fetch public profiles
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            target_user_id = request.query_params.get('user_id')
            
            if target_user_id:
                # Fetch specified user's info
                user = User.objects.get(id=target_user_id)
            else:
                # Fetch own info
                if not request.user.is_authenticated:
                    return Response({'result': False, 'msg': 'Not authenticated'})
                user = request.user
                
            user_profile = UserProfile.objects.get(user=user)
            
            return Response({
                'result': True,
                'msg': 'Success',
                'data': {
                    'user_id': user.id,
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.profile,
                }
            })
        except User.DoesNotExist:
             return Response({'result': False, 'msg': 'User not found'})
        except Exception as e:
            return Response({'result': False, 'msg': str(e)})