from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^hexminton/', include('badminton.urls'), name='hexminton'),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^admin/', admin.site.urls),
                       )
