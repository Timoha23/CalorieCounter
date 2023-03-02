from django.contrib import admin
from django.urls import path, include

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calories.urls')),
    path('', include('users.urls')),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.internal_server_error'


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),) 
