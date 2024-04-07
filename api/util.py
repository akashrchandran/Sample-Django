from rest_framework.response import Response
from rest_framework.permissions import BasePermission

def CustomResponse(status, messages = "", response = None):
    error = True if messages else False
    return Response(
        {
            "error": error,
            "status_code": status,
            "messages": messages,
            "response": response
        },
        status=status,
    )