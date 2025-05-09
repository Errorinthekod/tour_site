from django.http import HttpResponse
import asyncio
from django.views.generic import CreateView
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, viewsets

from .forms import SignUpForm
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from ..telegram_bot.bot import send_telegram_verification_link

User = get_user_model()


"""Registration"""


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegisterViewSet(viewsets.mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        Response({'message': 'https://web.telegram.org/k/#@team_four_bot'})
        if serializer.is_valid():
            user = serializer.save()
            try:
                asyncio.run(send_telegram_verification_link(user.telegram_chat_id, user.telegram_verification_token))
            except Exception as e:
                print("Ошибка при отправке в Telegram:", e)
            return Response({'message': 'User registered. Check Telegram for verification.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""
class RegisterView(generics.CreateAPIView):
    HttpResponse("@team_four_bot")
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
"""

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



"""
Users List
"""

class UserListViewSet(viewsets.ModelViewSet):  # ModelViewSet
    queryset = User.objects.all().order_by('username')  # Вывод данных в обратном порядке
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]




class TelegramVerificationView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(telegram_verification_token=token)
            user.is_verified_by_telegram = True
            user.save()
            return Response({'message': 'Telegram account verified successfully.'})
        except User.DoesNotExist:
            return Response({'error': 'Invalid verification token.'}, status=status.HTTP_400_BAD_REQUEST)



"""Келечекте бул файл өзгөрүш мүмкүн"""


