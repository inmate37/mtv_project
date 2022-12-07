# Django
from django.conf import settings
from django.contrib import admin
from django.urls import (
    include,
    path
)

# First party
from main.views import (
    index,
    simple
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple', simple),
    path('', index)
]
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
