from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
# Compare this snippet from lms_project/lms/views.py:
