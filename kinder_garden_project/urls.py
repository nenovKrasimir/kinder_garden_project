from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls
from for_parents import urls as parents_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('za_roditeli/', include(parents_urls))
]
