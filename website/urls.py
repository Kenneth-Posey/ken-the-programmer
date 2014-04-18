from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# from website_main.views.home import home
# from website_main.views.jspositioning import jspositioning
# from website_main.views.moving_text import moving_text
from website_main.views.under_construction import under_construction

urlpatterns = patterns('',
    # Examples:
    # url(r'^/*$', under_construction),
    url(r'^/*$', redirect_to, {'url': '/home/'}),
    # url(r'^home/*$', home),    
    
    # url(r'^moving_text/*$', moving_text),
    # url(r'^position/*$', jspositioning),

    # Django Urls
    url(r'^admin/', include(admin.site.urls)),
    
    # Zinnia Urls
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^home/tags/', include('zinnia.urls.tags')),
    url(r'^home/feeds/', include('zinnia.urls.feeds')),
    url(r'^home/authors/', include('zinnia.urls.authors')),
    url(r'^home/categories/', include('zinnia.urls.categories')),
    url(r'^home/comments/', include('zinnia.urls.comments')),
    url(r'^home/', include('zinnia.urls.entries')),
    url(r'^home/', include('zinnia.urls.archives')),
    url(r'^home/', include('zinnia.urls.shortlink')),
    url(r'^home/', include('zinnia.urls.quick_entry')),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

