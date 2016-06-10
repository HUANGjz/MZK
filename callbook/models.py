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
		
class Tag(models.Model):
	name = models.CharField(max_length=100)
	callbook = models.ManyToManyField(CallBook)
	def __str__(self) :
		return self.name

class PicPath(models.Model):
	name = models.ForeignKey(CallBook)
	file_path = models.CharField(max_length=500)
	
	def __str__(self) :
		return self.name.name + " " + self.file_path

class FirstCatalog(models.Model):
	name = models.ForeignKey(Tag)
	if_second = models.BooleanField()
	if_event = models.BooleanField()	
	
	def __str__(self) :
		return self.name.name

class SecondCatalog(models.Model):
	name = models.ForeignKey(Tag)
	firstcatalog_name = models.ForeignKey(FirstCatalog)
	
	def __str__(self) :
		return self.name.name
		

		




