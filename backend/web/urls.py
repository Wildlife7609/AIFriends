from django.urls import path, re_path
from web.views.index import index
from web.views.user.account.login import LoginView
from web.views.user.account.register import RegisterView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.get_user_info import GetUserInfoView
from web.views.user.profile.update import UpdateProfileView

from web.views.create.character.create import CharacterCreateView
from web.views.create.character.update import CharacterUpdateView
from web.views.create.character.get_single import CharacterGetSingleView
from web.views.create.character.remove import CharacterRemoveView

urlpatterns = [
    path('api/user/account/login/', LoginView.as_view(), name='user_account_login'),
    path('api/user/account/register/', RegisterView.as_view(), name='user_account_register'),
    path('api/user/account/logout/', LogoutView.as_view(), name='user_account_logout'),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view(), name='user_account_token_refresh'),
    path('api/user/account/get_user_info/', GetUserInfoView.as_view(), name='user_account_get_user_info'),
    path('api/user/profile/update/', UpdateProfileView.as_view(), name='user_profile_update'),
    
    # Character CRUD
    path('api/create/character/create/', CharacterCreateView.as_view(), name='character_create'),
    path('api/create/character/update/', CharacterUpdateView.as_view(), name='character_update'),
    path('api/create/character/get_single/', CharacterGetSingleView.as_view(), name='character_get_single'),
    path('api/create/character/remove/', CharacterRemoveView.as_view(), name='character_remove'),
    
    path('', index, name='index'),
    re_path(r'^(?!media/|static/|assets/).*$', index)
]