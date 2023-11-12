from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chaining/", include("smart_selects.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("auth/", include("apps.user.urls")),
    path("product/", include("apps.products.urls")),
    path("", include("apps.main.urls"))
]
urlpatterns += yasg_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
