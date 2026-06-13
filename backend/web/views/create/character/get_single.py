from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from web.models.character import Character

class CharacterGetSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            character_id = request.query_params.get('character_id')
            if not character_id:
                return Response({
                    'result': False,
                    'msg': 'Character ID is required.'
                })

            try:
                # Ensure only the author can fetch their own character data for editing
                character = Character.objects.get(id=character_id, author__user=request.user)
            except Character.DoesNotExist:
                return Response({
                    'result': False,
                    'msg': 'Character not found or you do not have permission to view it.'
                })

            data = {
                'id': character.id,
                'name': character.name,
                'photo': character.photo.url,
                'prompt': character.prompt,
                'background_image': character.background_image.url,
                'is_public': character.is_public,
                'greeting': character.greeting,
                'profile': character.profile,
                'tags': character.tags,
                'voice_id': character.voice_id,
            }

            return Response({
                'result': True,
                'msg': 'Success',
                'data': data
            })

        except Exception as e:
            return Response({
                'result': False,
                'msg': str(e)
            })
