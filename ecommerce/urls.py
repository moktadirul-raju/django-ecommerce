"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from .views import HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view(), name='home'),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include('accounts.urls'), name='account'),
    path('accounts/', include('accounts.password.urls')),
    path('', include('analytics.urls'), name='analytics'),
    path('products/', include('products.urls')),
    path('', include('search.urls')),
    path('', include('tags.urls')),
    path('cart/', include('carts.urls')),
    path('', include('orders.urls'), name='order'),
    path('', include('billing.urls')),
    path('', include('address.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
