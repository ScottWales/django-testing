from django.db import models

# Create your models here.

class Dataset(models.Model):
    """
    A dataset on the remote Thredds server
    """
    url = models.CharField(max_length=2048)
