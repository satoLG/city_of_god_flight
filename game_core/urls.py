from django.urls import path, re_path

from game_core.views import game_page

urlpatterns = [
    re_path(r'', game_page, name='main')
]
