from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class Index(APIView):
    """
    Index API View | Public
    """
    def get(self, request):
        content = {'message': 'Welcome To Social Media App'}
        return Response(content)


class SignupAPIView(APIView):
    """"
    Signup API to create a new user in DB
    """
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)  # Serialize and validate the data
        if serializer.is_valid():
            user = serializer.save()  # If data is valid, user will be created successfully
            return Response({'success': 'User {} was created successfully'.format(user.email)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)