"""
Defines the URL routes for this app.
"""


from django.urls import include, path, re_path
from rest_framework import routers

from . import views as lang_pref_api_views

RELEASED_LANGUAGES = lang_pref_api_views.LangPrefView.as_view({
    'get': 'get_released_languages',
})

LANG_PREF_API_ROUTER = routers.DefaultRouter()
LANG_PREF_API_ROUTER.register(r'lang_pref', lang_pref_api_views.LangPrefView)

urlpatterns = [
    path('v1/released_languages', RELEASED_LANGUAGES,
         name='released_languages_api'
         ),
]
