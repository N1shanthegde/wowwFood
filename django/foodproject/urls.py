from django.contrib import admin
from django.urls import include, path

from food.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('food/', include('food.urls', namespace='food')),
]

