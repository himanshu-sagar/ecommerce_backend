from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Index(APIView):
    #permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Welcome To Social Media App'}
        return Response(content)
