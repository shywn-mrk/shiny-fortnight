from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    delivery_time = models.PositiveIntegerField(max_length=90)
    delivered_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.vendor.name


class Trip(models.Model):
    status_values = [
        ("DELIVERED", "delivered"), 
        ("PICKED", "picked"),
        ("VENDOR_AT", "vendor_at"),
        ("ASSIGNED", "assigned"),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=9, choices=status_values) 


class DelayReport(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
