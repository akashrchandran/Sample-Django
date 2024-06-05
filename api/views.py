from django.contrib.auth.models import User
from django.http import FileResponse
from rest_framework import status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from . import schema
from .models import File, Product
from .serializers import (ArithmeticSerializer, DummySerializer,
                          FileSerializer, LoginSerializer, ProductSerializer,
                          UserSerializer)
from .util import CustomResponse


@schema.register_schema
class RegisterView(views.APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return CustomResponse(response="User successfully created", status=status.HTTP_201_CREATED)
        return CustomResponse(messages=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@schema.login_schema
class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.validated_data['username'])
            refresh = RefreshToken.for_user(user)
            return CustomResponse(response={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return CustomResponse(messages=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@schema.file_upload_schema
class UploadFileView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def post(self, request):
        files = request.FILES.getlist('files')  # Get the list of files
        file_models = []
    
        for file in files:
            if file.size > 5000000:  # limit file size to 5MB
                return CustomResponse(messages='One or more files are too large', status=status.HTTP_400_BAD_REQUEST)
    
            file_model = File(file=file, user=request.user, name=file.name, file_type=file.content_type)
            file_model.save()
            file_models.append(file_model)
    
        return CustomResponse(response=FileSerializer(file_models, many=True).data, status=status.HTTP_201_CREATED)

@schema.download_file_schema
class DownloadFileView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DummySerializer

    def get(self, request, pk):
        try:
            file = File.objects.get(pk=pk)
            return FileResponse(file.file, as_attachment=True)
        except File.DoesNotExist:
            return CustomResponse(messages='File not found', status=status.HTTP_404_NOT_FOUND)
        
class GetAllFilesView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DummySerializer

    def get(self, request):
        files = File.objects.filter(user=request.user)
        return CustomResponse(response=FileSerializer(files, many=True).data, status=status.HTTP_200_OK)
    
@schema.add_schema
class AddView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArithmeticSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data.get('num1')
            num2 = serializer.validated_data.get('num2')
            return CustomResponse(response=num1 + num2, status=status.HTTP_200_OK)
        else:
            return CustomResponse(messages=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@schema.subtract_schema
class SubtractView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArithmeticSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data.get('num1')
            num2 = serializer.validated_data.get('num2')
            return CustomResponse(response=num1 - num2, status=status.HTTP_200_OK)
        else:
            return CustomResponse(messages=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@schema.multiply_schema
class MultiplyView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArithmeticSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data.get('num1')
            num2 = serializer.validated_data.get('num2')
            return CustomResponse(response=num1 * num2, status=status.HTTP_200_OK)
        else:
            return CustomResponse(messages=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@schema.divide_schema
class DivideView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArithmeticSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data.get('num1')
            num2 = serializer.validated_data.get('num2')
            if num2 == 0:
                return CustomResponse(messages='Cannot divide by zero', status=status.HTTP_400_BAD_REQUEST)
            return CustomResponse(response=num1 / num2, status=status.HTTP_200_OK)
        else:
            return CustomResponse(messages=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@schema.product_schema
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]