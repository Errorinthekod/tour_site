from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import TourViewSet, RatingViewSet, TourCreateViewSet

router = DefaultRouter()
router.register(r'tour_list', TourViewSet, basename='tour_list') # | Просмотр туров
router.register(r'tour_create', TourCreateViewSet, basename='tour_create') # | Создание туров
router.register(r'ratings', RatingViewSet, basename='rating') # | Просмотр и создание рейтингов

urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),

    ]


"""Келечекте бул файл өзгөрүш мүмкүн"""




