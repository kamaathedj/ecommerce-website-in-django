from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path


urlpatterns = [
    path('',views.index,name='index'),
    path('wood/detail/<id>',views.details),
    path('payments/<id>',views.amPaying),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
