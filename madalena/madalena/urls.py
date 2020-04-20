from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import routers

from funnel.api.viewsets import FunnelViewSet
from resizer.views import TestView

admin.site.site_header = f'Madalena Admin'.upper()
admin.site.site_title =  f'Madalena Admin'
admin.site.index_title = f'Madalena Admin'
admin.empty_value_display = '**Empty**'

router = routers.DefaultRouter()
router.register(r'funnel', FunnelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('test/', TestView.as_view()),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
