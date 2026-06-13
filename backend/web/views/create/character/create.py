from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from web.models.user import UserProfile
from web.models.character import Character

class CharacterCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                return Response({
                    'result': False,
                    'msg': 'User profile not found.'
                })
            name = request.data.get('name', '').strip()
            profile = request.data.get('profile', '').strip()[:100000]
            is_public_raw = request.data.get('is_public')
            is_public = str(is_public_raw).lower() == 'true' if is_public_raw is not None else False
            prompt = request.data.get('prompt', '').strip()
            greeting = request.data.get('greeting', '').strip()[:500]
            tags = request.data.get('tags', '').strip()[:500]
            voice_id = request.data.get('voice_id', '').strip()[:100]

            # File inputs
            photo = request.FILES.get('photo', None)
            background_image = request.FILES.get('background_image', None)

            if not name:
                return Response({
                    'result': False,
                    'msg': 'Name is required.'
                })
            if not photo:
                return Response({
                    'result': False,
                    'msg': 'Photo is required.'
                })
            if not background_image:
                return Response({
                    'result': False,
                    'msg': 'Background image is required.'
                })
            if not profile:
                return Response({
                    'result': False,
                    'msg': 'Profile is required.'
                })

            character = Character.objects.create(
                author=user_profile,
                name=name,
                photo=photo,
                prompt=prompt,
                background_image=background_image,
                is_public=is_public,
                greeting=greeting,
                profile=profile,
                tags=tags,
                voice_id=voice_id
            )

            return Response({
                'result': True,
                'msg': 'Character created successfully!',
                'data': {
                    'id': character.id
                }
            })
        except Exception as e:
            return Response({
                'result': False,
                'msg': str(e)
            })

