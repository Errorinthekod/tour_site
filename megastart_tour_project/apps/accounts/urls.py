from django.urls import include , path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *




router = DefaultRouter()
router.register(r'user_list', UserListViewSet, basename='tours') # Просмотр пользователе            й
router.register(r'register', RegisterViewSet, basename='register')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify-telegram/<uuid:token>/', TelegramVerificationView.as_view(), name='verify-telegram'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


"""Келечекте бул файл өзгөрүш мүмкүн"""