from django.db import models


class Sensor(models.Model):
    owner_name=models.CharField(max_length=20, null=True, blank=True)
    contact= models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Sensor_ID:{self.id}"

class Sample(models.Model):
    sensor= models.ForeignKey(Sensor,on_delete = models.SET_NULL, null=True,)
    nitrogen = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)    
    potassium = models.FloatField(null=True, blank=True)
    pH = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True)
    csv_file= models.FileField(upload_to='sample_csv_files/', null=True, blank=True)
    
    def __str__(self):
        return f" Sample {self.id}"