from django.urls import path
from myapp import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns=[
    path('',views.IndexView.as_view(), name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)


