from django.contrib import admin
from django.urls import include, path

from resp import views as resp_views


urlpatterns = [
    path('html/', resp_views.html),
    path('json/', resp_views.json),
    path('resp/', include('resp.urls')),
    path('admin/', admin.site.urls),
]
