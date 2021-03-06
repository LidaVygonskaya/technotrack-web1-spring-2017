"""application URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core.views import HomePageView, RegisterView
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('blogs.urls', namespace = "blogs")),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/$', logout, {'template_name': 'core/logout.html'}, name="logout"),
    url(r'^accounts/register1/$', RegisterView.as_view(), name='register'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'), name="meow"),
]

if settings.DEBUG is True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

