from django.db import models
from django.utils import timezone
# Create your models here.

class Review(models.Model):
	name = models.CharField(max_length=20)
	#username = models.CharField(max_length=20)
	review = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return 'Name:{}'.format(self.name)

class Car_Info(models.Model):
	CarName = models.CharField(max_length=50)
	length = models.CharField(max_length=10, blank=True)
	widht = models.CharField(max_length=10, blank=True)
	height = models.CharField(max_length=10, blank=True)
	wheel_base = models.CharField(max_length=10, blank=True)
	ground_clearance = models.CharField(max_length=10, blank=True)
	Boot_capacity = models.CharField(max_length=10, blank=True)
	Fuel_type = models.CharField(max_length=10, blank=True)
	Engine_displacement = models.CharField(max_length=10, blank=True)
	Engine_type = models.CharField(max_length=30, blank=True)
	Max_power = models.CharField(max_length=20, blank=True)
	
	def __str__(self):
		return self.CarName