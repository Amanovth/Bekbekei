from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
from .services import teleorder, teleordercancel

class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['status'] = 'Cancel'

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=request.user)
            teleorder(order.id, order.first_name, order.last_name, order.number, order.product_for_order.all())
            return Response({"response": True})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OrdersListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
    

class OrderCancelView(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        try:
            order = Order.objects.get(pk=order_id)
            if order.user == request.user:
                order.status = 'Cancel'
                order.save()
                teleordercancel(order.id)
                return Response({"message": f"Заказ отменён!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "У вас нет прав чтобы отменять данный заказ!"}, status=status.HTTP_403_FORBIDDEN)
        except Order.DoesNotExist:
            return Response({"error": "Заказ не найден!"}, status=status.HTTP_404_NOT_FOUND)