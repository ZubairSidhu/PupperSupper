from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('puppersupperdev/', include('puppersupperdev.urls')),
    path('admin/', admin.site.urls),
]