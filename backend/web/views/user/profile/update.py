from django.utils.timezone import now
from web.models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from web.views.utils.photo import remove_old_photo
from web.models.user import User

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            username = request.data.get('username', '').strip()
            profile = request.data.get('profile', '').strip()[:500]
            photo = request.FILES.get('photo', None)

            if not username:
                return Response({"result": False, "msg": "Username is required"}, status=400)
            if not profile:
                return Response({"result": False, "msg": "Profile is required"}, status=400)
            if username != user.username and User.objects.filter(username=username).exists():
                return Response({"result": False, "msg": "Username already exists"}, status=401)
            if photo:
                remove_old_photo(user_profile.photo)
                user_profile.photo = photo

            user.username = username
            user_profile.profile = profile
            user_profile.update_time = now()
            user_profile.save()
            user.save()
            return Response({
            "result":True,
            "msg":"Profile updated successfully",
            "data":{
                "user_id":user.id,
                "username":user.username,
                "photo":user_profile.photo.url,
                "profile":user_profile.profile,
            },
            })
        except Exception as e:
            return Response({"result":False,"msg":str(e)},status=401)


