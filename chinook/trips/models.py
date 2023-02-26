from django.db import models

class River(models.Model):
    name = models.CharField(max_length=200)
    location  = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class TripType(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class RiverTrip(models.Model):
    river = models.ForeignKey(River, on_delete=models.CASCADE)
    trip_type = models.ForeignKey(TripType, on_delete=models.CASCADE)
    duration = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.river.name} - {self.trip_type.name}"