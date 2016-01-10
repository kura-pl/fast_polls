from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('polls.urls')),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^.*$', views.my_404, name='my_404')
]
