"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

'''Below import for file handling'''
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# File handling imports ends here

from django.contrib import admin
from django.urls import path
from pages.views import about_view,search_view,contact_view,social_view,model_form_upload,display_result


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_view, name='home'),
    path('about/', about_view),
    path('search/', search_view),
    path('social/', social_view),
    path('contact/', contact_view),
	path('upload/', model_form_upload),
	path('result/', display_result)
]


# Uploaded file storage handler
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# File storage handler ends here
