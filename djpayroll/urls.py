from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Pay Roll Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.payroll.urls'))
]
