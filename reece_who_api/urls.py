from django.conf.urls import include, url
from django.contrib import admin
from api.views import get_webhook_data

urlpatterns = [
    # Examples:
    # url(r'^$', 'reece_who_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reece_who_api/', get_webhook_data),
]
