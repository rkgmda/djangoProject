from django.db import models

# Create your models here.
class employees(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    addhar=models.CharField(max_length=16, unique=True)
    mobile_no=models.DecimalField(decimal_places=0,max_digits=10)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=True, null=False, blank=False)
    image=models.BinaryField (blank = True, null = True, editable = True)

    def __str__(self):
        return self.name