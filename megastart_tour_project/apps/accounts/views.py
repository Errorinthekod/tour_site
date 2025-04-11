from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


"""Registration"""

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer




class UserListViewSet(viewsets.ModelViewSet):  # ModelViewSet
    queryset = User.objects.all().order_by('username')  # Вывод данных в обратном порядке
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]

"""logout"""

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""Келечекте бул файл өзгөрүш мүмкүн"""


