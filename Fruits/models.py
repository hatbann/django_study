from django.db import models

# Create your models here.
class Fruits(models.Model):
    name = models.CharField(max_length=40, null=True,default='')
    descript = models.TextField(null=True,default='')
    price = models.FloatField(null=True,default='')
    quantity = models.IntegerField(null=True,default='')
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id = {}, name = {}, description : {}'.format(self.id, self.name, self.descript)