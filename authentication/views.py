from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class Index(APIView):
    def get(self, request):
        content = {'message': 'Welcome To Social Media App'}
        return Response(content)


class SignupAPIView(APIView):
    def post(self, request, *args, **kwargs):

        if request.data.get("password") != request.data.get("confirm_password"):
            return Response("Password and Confirm Password is not same", status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'success': 'User {} was created successfully'.format(user.email)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)