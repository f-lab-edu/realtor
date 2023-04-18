# from rest_framework.authtoken.models import Token
# from rest_framework import permissions
# from rest_framework.decorators import api_view
# from realtor.serializers import RegistrationUserSerializer

# @api_view(['POST',])
# @permissions_classes((permissions.AllowAny, ))
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationUserSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#             data['response'] = "successfully registered a new user"
#             data['email'] = account.email
#             data['username'] = account.username
#             token = Token.objects.get(user=account).key
#             data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)
