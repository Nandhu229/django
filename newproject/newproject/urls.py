"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from newapp import views as newviews
from django.conf.urls.static import static
from newproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',newviews.login,name='login'),
    path('viewdetails',newviews.viewdetails,name='viewdetails'),
    path('index',newviews.index,name='index'),
    path('hospital_details',newviews.hospital_details1,name='hospital_details1'),
    path('hospital1',newviews.hospital1,name='hospital1'),
    path('admin_hospitaldetails',newviews.admin_hospitaldetails,name='admin_hospitaldetails'),
    path('delete_viewdetails1/(?P<pk>\d+)$',newviews.delete_viewdetails1,name='delete_viewdetails1'),
    path('mydetails',newviews.mydetails,name='mydetails')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
