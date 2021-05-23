from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication_app.urls')),
    # path('my_admin', include('admin_section.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)