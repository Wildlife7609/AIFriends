from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'create_time', 'update_time')
    list_filter = ('create_time',)
    search_fields = ('user__username', 'user__email')
    ordering = ('-create_time',)
    readonly_fields = ('create_time', 'update_time')
          

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
    list_display = ('author', 'name', 'create_time')
    list_filter = ('author', 'create_time')
    search_fields = ('author__user__username', 'name')
    ordering = ('-create_time',)
    readonly_fields = ('create_time', 'update_time')
