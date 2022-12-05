from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
import os

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^_nested_admin/', include('nested_admin.urls')),
    path("accounts/", include("django.contrib.auth.urls")),  # Keep
    path("", include("home.urls")),
    path("wiki/", include("wiki.urls")),
    path("network/", include("network.urls")),
    path("auctions/", include("auctions.urls")),
    path("mail/", include("mail.urls")),
    path("ads/", include("ads.urls")),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(
        r"^site/(?P<path>.*)$",
        serve,
        {"document_root": os.path.join(BASE_DIR, "site"), "show_indexes": True},
        name="site_path",
    ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path(
        "favicon.ico",
        serve,
        {
            "path": "favicon.ico",
            "document_root": os.path.join(BASE_DIR, "home/static"),
        },
    ),
]
