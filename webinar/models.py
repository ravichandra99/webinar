from django.db import models

# Create your models here.
class JustUser(models.Model):
	fname = models.CharField(max_length = 30,verbose_name = 'First Name')
	lname = models.CharField(max_length = 30,verbose_name = 'Last Name')
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	college = models.CharField(max_length = 30,verbose_name = 'College/Organization')
	profession = models.CharField(max_length = 30,verbose_name = 'Profession')

	def __str__(self):
		return self.name