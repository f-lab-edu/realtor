from authentication.serializers import RegistrationSerializer
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import permissions, serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):

        try:
            data = ["message", "email", "username", "token"]
            registration_serializer = RegistrationSerializer(data=request.data)

            if registration_serializer.is_valid():
                user = registration_serializer.save()
                user.is_active = True
                user.save()
                token = Token.objects.get_or_create(user=user)[0].key
                data[0] = "user registered successfully"
                data[1] = user.email
                data[2] = user.username
                data[3] = token

            else:
                data = registration_serializer.errors

            return Response(data)

        except IntegrityError as e:
            user = User.objects.get(username="")
            user.delete()
            raise ValidationError({"400": f"{str(e)}"})

        except KeyError as e:
            print(e)
            raise ValidationError({"400": f"Field {str(e)} missing"})

        # return Response(
        #     {
        #         # "error": serializers.error,
        #         "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \ NON AUTHORITATIVE INFORMATION",
        #     }
        # )
