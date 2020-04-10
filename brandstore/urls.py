from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
     
    path('',include('website.urls')),
    path('admin/', admin.site.urls ),
    path('accounts/', include('allauth.urls')),
    path('', include('website.urls', namespace='website'))
]

 

