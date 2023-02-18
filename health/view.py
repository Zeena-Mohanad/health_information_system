from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from health.serializer import MySerializer
from rest_framework import status

class MyView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            # ...process the uploaded file...
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
