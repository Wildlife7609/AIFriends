from django.utils.timezone import now
from web.models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from web.views.utils.photo import remove_old_photo
from web.models.user import User
from django.db import transaction
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
                return Response({"result": False, "msg": "Username is required"})
            if not profile:
                return Response({"result": False, "msg": "Profile is required"})
            if username != user.username and User.objects.filter(username=username).exists():
                return Response({"result": False, "msg": "Username already exists"})
            old_photo = None
            if photo:
                old_photo = user_profile.photo
                user_profile.photo = photo

            user.username = username
            user_profile.profile = profile
            user_profile.update_time = now()
            
            # 引入 Django 的 transaction 原子锁
            with transaction.atomic():
                user_profile.save()
                user.save()
            
            # 全部安全落袋后，再动手删旧的！
            if old_photo:
                remove_old_photo(old_photo)
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
            return Response({"result":False,"msg":str(e)})


