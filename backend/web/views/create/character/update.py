from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from web.models.character import Character
from django.utils.timezone import now

class CharacterUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # 1. Get Character ID
            character_id = request.data.get('character_id')
            if not character_id:
                return Response({
                    'result': False,
                    'msg': 'Character ID is required.'
                })
            
            # 2. Find Character and Verify Ownership
            try:
                character = Character.objects.get(id=character_id, author__user=request.user)
            except Character.DoesNotExist:
                return Response({
                    'result': False,
                    'msg': 'Character not found or you do not have permission to edit it.'
                })

            # 3. Update Text Fields (only if provided in request)
            if 'name' in request.data:
                character.name = request.data.get('name', '').strip()
            
            if 'profile' in request.data:
                character.profile = request.data.get('profile', '').strip()[:100000]
                
            if 'prompt' in request.data:
                character.prompt = request.data.get('prompt', '').strip()
                
            if 'greeting' in request.data:
                character.greeting = request.data.get('greeting', '').strip()[:500]
                
            if 'tags' in request.data:
                character.tags = request.data.get('tags', '').strip()[:500]
                
            if 'voice_id' in request.data:
                character.voice_id = request.data.get('voice_id', '').strip()[:100]

            if 'is_public' in request.data:
                is_public_raw = request.data.get('is_public')
                character.is_public = str(is_public_raw).lower() == 'true'

            # 4. Update File Fields (only if new files are uploaded)
            if 'photo' in request.FILES:
                character.photo = request.FILES.get('photo')
                
            if 'background_image' in request.FILES:
                character.background_image = request.FILES.get('background_image')

            # 5. Update timestamp and save
            character.update_time = now()
            character.save()

            return Response({
                'result': True,
                'msg': 'Character updated successfully!',
                'data': {
                    'id': character.id
                }
            })
            
        except Exception as e:
            return Response({
                'result': False,
                'msg': str(e)
            })
