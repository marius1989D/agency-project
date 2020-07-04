from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    service_title = models.CharField(max_length=50)
    service_description = models.TextField(blank=True)

    def __str__(self):
        return self.service_title
