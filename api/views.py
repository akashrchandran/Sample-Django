from django.contrib.auth.models import User
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from .models import File
from .serializers import FileSerializer, UserSerializer
from .util import CustomResponse


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(**serializer.validated_data)
        return CustomResponse("User successfully created", status=status.HTTP_201_CREATED)
    return CustomResponse(messages = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        user = User.objects.get(username=request.data['username'])
        if user.check_password(request.data['password']):
            refresh = RefreshToken.for_user(user)
            return CustomResponse(response={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return CustomResponse(messages='Incorrect password', status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return CustomResponse(messages='User does not exist', status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return CustomResponse(messages="Server side error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_file(request):
    if 'file' not in request.data:
        return CustomResponse(messages='No file was included in the request', status=status.HTTP_400_BAD_REQUEST)
    file = request.data['file']
    if file.size > 5000000:  # limit file size to 5MB
        return CustomResponse(messages='The file is too large', status=status.HTTP_400_BAD_REQUEST)
    file_model = File(file=file, user=request.user)
    file_model.save()
    return CustomResponse(response=FileSerializer(file_model).data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_file(request, pk):
    try:
        file = File.objects.get(pk=pk)
        return FileResponse(file.file, as_attachment=True)
    except File.DoesNotExist:
        return CustomResponse(messages='File not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    num1 = request.data.get('num1')
    num2 = request.data.get('num2')
    if num1 is not None and num2 is not None:
        return CustomResponse(response=num1 + num2, status=status.HTTP_200_OK)
    else:
        return CustomResponse(messages='Both num1 and num2 are required', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subtract(request):
    num1 = request.data.get('num1')
    num2 = request.data.get('num2')
    if num1 is not None and num2 is not None:
        return CustomResponse(response=num1 - num2, status=status.HTTP_200_OK)
    else:
        return CustomResponse(messages='Both num1 and num2 are required', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def multiply(request):
    num1 = request.data.get('num1')
    num2 = request.data.get('num2')
    if num1 is not None and num2 is not None:
        return CustomResponse(response=num1 * num2, status=status.HTTP_200_OK)
    else:
        return CustomResponse(messages='Both num1 and num2 are required', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def divide(request):
    num1 = request.data.get('num1')
    num2 = request.data.get('num2')
    if num1 is not None and num2 is not None:
        if num2 == 0:
            return CustomResponse(messages='Cannot divide by zero', status=status.HTTP_400_BAD_REQUEST)
        return CustomResponse(response=num1 / num2, status=status.HTTP_200_OK)
    else:
        return CustomResponse(messages='Both num1 and num2 are required', status=status.HTTP_400_BAD_REQUEST)
