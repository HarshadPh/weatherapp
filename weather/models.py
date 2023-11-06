from django.db import models

# Create your models here.
class subscriber(models.Model):
    name=models.TextField()
    email = models.EmailField(max_length=255)
    mobile_no = models.CharField(max_length=15)  # You may want to validate the mobile number
    city = models.TextField()
    sub = models.TextField()

    def __str__(self):
        return self.name

