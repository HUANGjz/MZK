from django.db import models

# Create your models here.

class CallBook(models.Model):
	name = models.CharField(max_length=100)
	file_path = models.CharField(max_length=500)
	cnt = models.IntegerField()
	date_time = models.DateTimeField(auto_now_add = True)
	
	def __str__(self) :
		return self.name
	class Meta:
		ordering = ['-date_time']
