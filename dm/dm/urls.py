from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
#    (r'^hospital','dm.hospital.views.hospital'),
#    (r'^alpha','dm.hospital.views.graph',name='alpha'),
#    (r'^efficiency','dm.hospital.views.graph',name='efficiency'),
#    (r'^volume','dm.hospital.views.graph',name='volume'),
    # Examples:
    # url(r'^$', 'dm.views.home', name='home'),
    # url(r'^dm/', include('dm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = patterns('',
   url(r'^hospital','dm.hospital.views.hospital',name='user'),
   url(r'^alpha','dm.hospital.views.alpha',name='alpha'),
   url(r'^efficiency','dm.hospital.views.efficiency',name='efficiency'),
   url(r'^volume','dm.hospital.views.volume',name='volume'),
# Examples:
# url(r'^$', 'mysite.views.home', name='home'),
# url(r'^mysite/', include('mysite.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
		)
                   
