from django.db import models

class TeamSection(models.Model):
    team_title = models.CharField(max_length=200)
    team_subtitle = models.CharField(max_length=200)
    team_description = models.TextField(blank=True)



class Realtor(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
