from authentication.serializers import RegistrationSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):

        registration_serializer = RegistrationSerializer(data=request.data)

        if registration_serializer.is_valid():
            user = registration_serializer.save()
            user.is_active = True
            user.save()

            token = Token.objects.get_or_create(user=user)[0].key

            data = registration_serializer.data
            data["token"] = token

        else:
            data = registration_serializer.errors

        return Response(data)


class LoginView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    def post(self, request, *args, **kwargs):

        login_serializer = UserLoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)

        return Response(login_serializer.data, status=status.HTTP_200_OK)
