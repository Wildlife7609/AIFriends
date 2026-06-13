from web.views.utils.photo import remove_old_photo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from web.models.character import Character

class CharacterRemoveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            character_id = request.data.get('character_id')
            if not character_id:
                return Response({
                    'result': False,
                    'msg': 'Character ID is required.'
                })

            try:
                # Ensure only the author can delete their own character
                character = Character.objects.get(id=character_id, author__user=request.user)
            except Character.DoesNotExist:
                return Response({
                    'result': False,
                    'msg': 'Character not found or you do not have permission to delete it.'
                })

            # Delete the character from the database
            remove_old_photo(character.photo)
            remove_old_photo(character.background_image)
            character.delete()

            return Response({
                'result': True,
                'msg': 'Character deleted successfully!'
            })

        except Exception as e:
            return Response({
                'result': False,
                'msg': str(e)
            })
