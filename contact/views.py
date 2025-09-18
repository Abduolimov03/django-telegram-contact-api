from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from .models import ContactMessage
from .utils import send_telegram_message

class ContactApiView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():

            contact = serializer.save()

            send_telegram_message(
                contact.name,
                contact.phone,
                contact.email,
                contact.message
            )

            return Response({"success": "Xabar yuborildi!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
