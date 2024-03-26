from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, AssignmentViewSet, QuestionViewSet, ClassViewSet, UserAuthenticationView
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'classes', ClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('authenticate/', UserAuthenticationView.as_view(), name='authenticate'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
