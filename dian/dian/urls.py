from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',\
        namespace='rest_framework')),
    url(r'^api-token-auth/',\
        'rest_framework.authtoken.views.obtain_auth_token'),

    url(r'^account/', include('account.urls')),

    url(r'^table/', include('table.urls')),
    url(r'^regstration/', include('regstration.urls')),
)
