from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
from .services import teleorder, teleordercancel
from datetime import datetime
from django.views import View

class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime('%d.%m.%Y %H:%M')
            user = request.user
            order = serializer.save(user=user, first_name=user.first_name, last_name=user.last_name, number=user.phone, datetime=formatted_datetime)
            teleorder(order.id, order.first_name, order.last_name, order.number, order.product_for_order.all(), order.address, order.sum)
            return Response({"response": True})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OrdersListView(generics.ListAPIView):
    serializer_class = OrderListSrializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user, status__in=['New', 'InProgress', 'Done'])
    
class OrdersDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSrializer
    permission_classes = [IsAuthenticated]


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
        
# Адрес доставки

class DeliveryAddressCreateView(generics.CreateAPIView):
    serializer_class = DeliveryAddressSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response({"response": True})

class DeliveryAddressListView(generics.ListAPIView):
    serializer_class = DeliveryAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DeliveryAddress.objects.filter(user=self.request.user)
    
class DeliveryAddressDeleteView(generics.GenericAPIView):
    serializer_class = DeliveryAddressSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        delivery_id = self.kwargs.get('delivery_id')
        try:
            delivery = DeliveryAddress.objects.get(pk=delivery_id)
            if delivery.user == request.user:
                delivery.delete()
                return Response({"message": f"Удалено адрес доставки!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "У вас нет прав чтобы удалить данный адрес"}, status=status.HTTP_403_FORBIDDEN)
        except DeliveryAddress.DoesNotExist:
            return Response({"error": "Адрес не найден!"}, status=status.HTTP_404_NOT_FOUND)
        

class OrderTableView(View):
    def get(self, request):
        table = OrderTable.objects.all()
        order_info = OrderTableInfo.objects.all()
        return render(request, 'order/index.html', {'table': table, 'order_info': order_info})