from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	#propiedades
	#en ForeingKey en django 2 se agrego el parametro on_delete
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	tittle = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.tittle