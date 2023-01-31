from django.db import models

class member(models.Model):
	first_name = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	phone = models.IntegerField()
	password = models.CharField(max_length = 15, default='')

	def __str__(self):
		return self.first_name

