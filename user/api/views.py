from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from user.api.serializers import registrationSerializer
from rest_framework.authtoken.models import Token
from user import models
from rest_framework import status
from django.contrib import auth
# from user.models import Account
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET',])
# @permission_classes((IsAuthenticated,))
# def session_view(request):
#     if request.method == 'GET':
#         user = request.user
#         account = Account.objects.get(email=user)
#         data = {}
#         if account is not None:
#             data['response']= 'El usuario esta en sesion'
#             data['username']= account.username
#             data['email']= account.email
#             data['first_name']= account.first_name
#             data['last_name']= account.last_name
#             data['phone_number']= account.phone_number
#             refresh = RefreshToken.for_user(account)
#             data['token'] = {
#                 'refresh' : str(refresh),
#                 'access' : str(refresh.access_token)
#             }
#             return Response(data)
#         else:
#             data['error'] = 'El usuario no existe'
#             return Response (data, status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response (status=status.HTTP_200_OK) 




@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = registrationSerializer(data=request.data) 
        data = {}


        if serializer.is_valid():
            account = serializer.save()
            data['response']= 'el registro del usuario fue exitoso'
            data['username']= account.username
            data['email']= account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)