from django.urls import include , path
from .views import *

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]