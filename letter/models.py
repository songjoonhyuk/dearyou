from django.db import models

# Create your models here.
class Letter(models.Model):
	title = models.CharField(max_length=100)
	sender = models.CharField(max_length=50)
	recipient = models.CharField(max_length=50)
	content = models.TextField()
	address_sender = models.TextField()
	address_recipient = models.TextField()
	phone_sender = models.CharField(max_length=20)
	phone_recipient = models.CharField(max_length=20)

	def __str__(self):
		return self.title