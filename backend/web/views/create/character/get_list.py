from rest_framework.views import APIView
from rest_framework.response import Response
from web.models.character import Character
from web.models.user import UserProfile
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import AllowAny

class CharacterGetListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        try:
            # 1. Handle pagination offset
            items_count = int(request.query_params.get('items_count', 0))
            
            # 2. Check if user_id is provided
            user_id = request.query_params.get('user_id')
            
            filters = Q()
            if user_id:
                user = User.objects.get(id=user_id)
                user_profile = UserProfile.objects.get(user=user)
                
                # If logged in user is viewing their own list, show all characters
                if request.user.is_authenticated and request.user.id == int(user_id):
                    filters = Q(author=user_profile)
                else:
                    # Otherwise, only show public characters of this user
                    filters = Q(author=user_profile, is_public=True)
            else:
                # Default: show all public characters if no user_id is specified
                filters = Q(is_public=True)
                
            # 3. Fetch characters with limit and offset (20 items per page)
            character_raw = Character.objects.filter(filters).select_related('author', 'author__user').order_by('-id')[items_count:items_count + 20]
            
            # 4. Serialize data
            data = []
            for character in character_raw:
                author = character.author
                data.append({
                    'id': character.id,
                    'name': character.name,
                    'photo': character.photo.url if character.photo else '',
                    'background_image': character.background_image.url if character.background_image else '',
                    'profile': character.profile,
                    'greeting': character.greeting,
                    'tags': character.tags,
                    'chat_count': character.chat_count,
                    'is_public': character.is_public,
                    'create_time': character.create_time,
                    'author': {
                        'id': author.user.id,
                        'username': author.user.username,
                        'photo': author.photo.url if author.photo else '',
                    }
                })

            return Response({
                'result': True,
                'msg': 'Success',
                'data': data
            })

        except User.DoesNotExist:
             return Response({
                'result': False,
                'msg': 'User not found'
            })
        except Exception as e:
            return Response({
                'result': False,
                'msg': str(e)
            })
