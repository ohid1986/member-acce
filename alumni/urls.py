"""alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from  django.conf.urls.static import static


from django.views.generic import (
    RedirectView, TemplateView)

from member import urls as member_urls
from contact import urls as contact_urls
from user import urls as user_urls


urlpatterns = [


    # url(r'^$',
    #     RedirectView.as_view(
    #         pattern_name='blog_post_list',
    #         permanent=False)),
    url(r'^about/$',
        TemplateView.as_view(
            template_name='site/about.html'),
        name='about_site'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(member_urls)),
    url(r'^contact/', include(contact_urls)),

    url(r'^user/',
        include(
            user_urls,
            app_name='user',
            namespace='dj-auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







