from backend import settings
import os
def remove_old_photo(photo):
    if photo and photo.name != "static/images/default.jpg":
        old_path = settings.MEDIA_ROOT / photo.name
        if os.path.exists(old_path):
            os.remove(old_path)
    