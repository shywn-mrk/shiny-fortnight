from rest_framework import serializers

from marketplace.models import DelayReport, Order, Trip, Vendor


class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"


class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = "__all__"


class DelayReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DelayReport
        fields = "__all__"
