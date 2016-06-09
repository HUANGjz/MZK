from django.db import models

# Create your models here.

class CallBook(models.Model):
	name = models.CharField(max_length=100)
	cnt = models.IntegerField()
	date_time = models.DateTimeField(auto_now_add = True)
	singer = models.CharField(max_length=100)
	
	def __str__(self) :
		return self.name
	class Meta:
		ordering = ['-date_time']

class PicPath(models.Model):
	name = models.CharField(max_length=100)
	file_path = models.CharField(max_length=500)
	
	def __str__(self) :
		return self.name + " " + self.file_path

class EventCatalog(models.Model):
	name = models.CharField(max_length=100)
	if_second = models.BooleanField()
	
	def __str__(self) :
		return self.name

class SingerCatalog(models.Model):
	name = models.CharField(max_length=100)
	if_second = models.BooleanField()
	
	def __str__(self) :
		return self.name

class SecondCatalog(models.Model):
	name = models.CharField(max_length=100)
	firstcatalog_name = models.CharField(max_length=100)
	
	def __str__(self) :
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	tag_name = models.CharField(max_length=100)
	
	def __str__(self) :
		return self.name + " " + self.tag_name

		




