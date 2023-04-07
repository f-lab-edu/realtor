from authentication.serializers import RegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions, serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        registration_serializer = RegistrationSerializer(data=request.data)

        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if registration_serializer.is_valid():
            user = registration_serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    # "user": {
                    #     "id": serializers.data["id"],
                    #     "first_name": serializers.data["first_name"],
                    #     "last_name": serializers.data["last_name"],
                    #     "username": serializers.data["username"],
                    #     "email": serializers.data["email"],
                    #     "is_active": serializers.data["is_active"],
                    #     "is_staff": serializers.data["is_staff"],
                    # },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                }
            )
        print(User.objects.all())
        print(registration_serializer.errors)
        print(registration_serializer.is_valid())
        return Response(
            {
                # "error": serializers.error,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \ NON AUTHORITATIVE INFORMATION",
            }
        )
