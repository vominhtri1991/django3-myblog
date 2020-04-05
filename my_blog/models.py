from django.db import models

class Blog(models.Model):
	title=models.CharField(max_length=120)
	description=models.CharField(max_length=120)
	date=models.DateField()
	content=models.TextField()

	def __str__(self):
		return "Blog "+str(self.id)+": "+self.title
# Create your models here.
