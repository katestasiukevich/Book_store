"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from goods import views as goods_views

app_name = "proj"
urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('refs/', include("refs.urls", namespace="references")),
    path('goods/', include("goods.urls", namespace="goods")),
    path('accounts/', include("acc.urls", namespace="accounts")),

    path('contact-us/', goods_views.contact_form, name="contact-us"),
    path('message-sent/', goods_views.message_sent, name="message-sent"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
