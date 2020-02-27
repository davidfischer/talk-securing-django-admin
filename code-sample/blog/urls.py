from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from .admin import admin_site


urlpatterns = [
    # Use a customized admin site (see blog/admin.py)
    # You can customize precisely which models are added even third party apps
    path("", admin_site.urls),
]


if settings.ADMIN_ENABLED:
    urlpatterns += [
        # Redirect the admin login to a different login URL
        # This login URL could enforce two-factor auth or use rate-limiting
        # See django-allauth
        #path(
        #    f"{settings.ADMIN_URL}/login/",
        #    RedirectView.as_view(url=settings.LOGIN_URL),
        #),

        # Includes the default admin site (Users, Groups)
        path(f"{settings.ADMIN_URL}/", admin.site.urls),
    ]
