from django.urls import path
from web.views.index import index
from web.views.user.account.login import LoginView
from web.views.user.account.register import RegisterView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView

urlpatterns = [
    path('api/user/login/', LoginView.as_view(), name='user_login'),
    path('api/user/register/', RegisterView.as_view(), name='user_register'),
    path('api/user/logout/', LogoutView.as_view(), name='user_logout'),
    path('api/user/token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('', index, name='index'),
]