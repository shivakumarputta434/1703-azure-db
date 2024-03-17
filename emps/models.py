from django.db import models

class SiteUsers(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    class Meta():
        db_table='site_users'
