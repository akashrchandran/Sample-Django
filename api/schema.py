from drf_spectacular.utils import extend_schema

from api import serializers

register_schema = extend_schema(
    description="Create a new user",
    request=serializers.UserSerializer,
)

login_schema = extend_schema(
    description="Authenticate a user",
    request=serializers.LoginSerializer,
)

file_upload_schema = extend_schema(
    description="Upload a file",
    request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "file": {"type": "string", "format": "binary"}},
            },
        },
)

download_file_schema = extend_schema(
    description="Download a file using the file ID",
)

add_schema = extend_schema(
    description="Add two numbers",
    request=serializers.ArithmeticSerializer,
)

subtract_schema = extend_schema(
    description="Subtract two numbers",
    request=serializers.ArithmeticSerializer,
)

multiply_schema = extend_schema(
    description="Multiply two numbers",
    request=serializers.ArithmeticSerializer,
)

divide_schema = extend_schema(
    description="Divide two numbers",
    request=serializers.ArithmeticSerializer,
)

product_schema = extend_schema(
    description="Operations with Products",
    responses={200: serializers.ProductSerializer(many=True)},
    request=serializers.ProductSerializer,
)

get_all_files_schema = extend_schema(
    description="Get all files",
)