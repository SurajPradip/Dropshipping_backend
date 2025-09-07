from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .msg import msg

class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    msg = msg()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "status": True,
                "msg": self.msg.success_msg,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": False,
            "msg": self.msg.error_msg,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class ListProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return Response({
            "status": True,
            "msg": "Products retrieved successfully",
            "response": serializer.data
        }, status=status.HTTP_200_OK)