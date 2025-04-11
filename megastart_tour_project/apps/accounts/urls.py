from django.urls import include , path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *



router = DefaultRouter()
router.register(r'user_list', UserListViewSet, basename='tours') # Просмотр пользователе            й


urlpatterns = [
    path('user_management/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


"""Келечекте бул файл өзгөрүш мүмкүн"""