"""
Definition of urls for ashlyn_site.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import home.forms
import home.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Website Base:
    url(r'^', include('home.urls')),

    # Django admin page
    url(r'^admin/', include(admin.site.urls)),
]
