from django.urls import path
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('niji.urls')),
]
