from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Router.urls')),
    path('', include('TestApp.urls')),
    path('', include('Socnet.urls')),
    path('', include('Test_API.urls')),
    path('', include('Wikipedia.urls')),
]
