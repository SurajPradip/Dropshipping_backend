from rest_framework import generics,status
from rest_framework.response import Response
from .msg import msg

class PingingView(generics.GenericAPIView):
    msg = msg()
    def get(self, request, *args, **kwargs):
        return Response({"status":True,"msg":self.msg.success_msg,
                "response":"First API is working fine"},status=status.HTTP_200_OK)
