from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^artrecommender/', include('artrecommender.urls')),
    url(r'^admin/', admin.site.urls),
]