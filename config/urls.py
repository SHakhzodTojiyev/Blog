from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

handler404 = 'blog.views.handler_404'