from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.static import serve as static_serve

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    url(r'account/', include('fantasybooking.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social_django.urls', namespace='social')),
    url(r'', include('fantasybooking.home.urls')),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^__debug__/', include(debug_toolbar.urls)),
   ] # noqa
