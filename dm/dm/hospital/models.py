from django.db import models
from django.forms import ModelForm
class hosp(models.Model):
    Number_Of_Bed=models.CharField(max_length=100)
    Operation_Room=models.CharField(max_length=100)
    Efficiency_Index=models.CharField(max_length=100)
    Data=models.FileField(upload_to="documents/",blank=True)
    Casuality=models.CharField(max_length=100,blank=True)
    def __unicode__(self):

	 return str(self.Number_Of_Bed)+'/'+str(self.Operation_Room)+'/'+str(self.Efficiency_Index)+'/'+str(self.Casuality)

class hospForm(ModelForm):
    class Meta:
	model=hosp


# Create your models here.
