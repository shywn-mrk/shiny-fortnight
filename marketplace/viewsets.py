import requests

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.response import Response

from marketplace.models import Trip, DelayReport, Vendor, Order
from marketplace.serializers import DelayReportSerializer, OrderSerializer, TripSerializer, VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


class DelayReportViewSet(viewsets.ModelViewSet):
    serializer_class = DelayReportSerializer
    queryset = DelayReport.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()

        trips = Trip.objects.filter(order=order, status__in=['ASSIGNED VENODR_AT', 'PICKED'])
        if trips.exists():
            mock_api_url = "https://run.mocky.io/v3/122c2796-5df4-461c-ab75-87c1192b17f7"
            response = requests.get(mock_api_url)

            if response.status_code == 200:
                new_delivery_estimate = response.json().get('eta')
                order.time_delivery = new_delivery_estimate
                order.save()

                delay_report = DelayReport.objects.create(order=order)
                delay_report_serializer = DelayReportSerializer(delay_report)

                return Response(
                    {
                        "message": "New delivery estimate calculated and order updated.",
                        "delay_report": delay_report_serializer.data
                    },
                    status=status.HTTP_200_OK
                )
        else:
            delay_report = DelayReport.objects.create(order=order)
            delay_report_serializer = DelayReportSerializer(delay_report)

            return Response(
                {
                    "message": "Order placed in the delay queue.",
                    "delay_report": delay_report_serializer.data
                },
                status=status.HTTP_200_OK
            )
