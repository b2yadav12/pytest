from django.contrib import admin
from django.urls import include, path

from resp import views as resp_views


urlpatterns = [
    path('', resp_views.html),
    path('json/', resp_views.json),
    path('save-persion', resp_views.createPerson),
    path('persion-list', resp_views.personList),
    path('search-persion/<first_name>', resp_views.filterPersion),
    path('get-persion/<id>', resp_views.getPersion),
    path('resp/', include('resp.urls')),
    path('admin/', admin.site.urls),
]
